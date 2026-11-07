#!/usr/bin/env python3
"""数据集目录查询、固定版本下载和文件校验。仅使用Python标准库。"""
import argparse
from collections import Counter
import csv
import datetime as dt
import hashlib
import gzip
import io
import json
from pathlib import Path
import sys
import tarfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def catalog():
    return read_json(ROOT / 'catalog.json')['datasets']


def choose(identifier):
    matches = [r for r in catalog() if r['id'] == identifier]
    if not matches:
        raise ValueError(f'未知数据集 {identifier!r}；运行 list 查看ID。')
    return matches[0]


def safe_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError('资产路径越过仓库根目录。')
    return path


def records(path):
    """兼容作者把JSONL文件命名为.json的情况，不执行pickle等格式。"""
    if '.part' in path.suffix:
        raise ValueError('该文件为归档分片；请先运行 restore <数据集ID>。')
    if path.name.endswith(('.tgz','.tar.gz')):
        with tarfile.open(path,'r:gz') as archive:
            yield {'archive':path.name,'members':[m.name for _,m in zip(range(25),archive)]}
        return
    if path.suffix.lower()=='.gz':
        with gzip.open(path,'rt',encoding='utf-8') as stream:
            for line in stream:
                if line.strip():
                    yield {'raw_line':line.rstrip('\r\n'),'columns':line.rstrip('\r\n').split('\t')}
        return
    if path.suffix.lower() in {'.pkl','.pickle','.npy','.npz'}:
        # 不自动反序列化pickle或含object的NumPy数据，以免执行上游对象代码。
        yield {'file':path.name,'bytes':path.stat().st_size,'note':'已保存原始二进制数据；查看样本请在可信研究环境使用作者的数据加载器。'}
        return
    if path.suffix.lower() == '.zip':
        with zipfile.ZipFile(path) as archive:
            names=[n for n in archive.namelist() if n.endswith(('.jsonl','.json')) and not n.startswith('__MACOSX/')]
            if not names:
                yield {'archive':path.name,'members':[n for n in archive.namelist() if not n.endswith('/')][:25]}
                return
            name=next((n for n in names if n.endswith('/train.jsonl')),names[0])
            with archive.open(name) as stream:
                for line in io.TextIOWrapper(stream,encoding='utf-8-sig'):
                    if line.strip():
                        yield {'archive_member':name,'record':json.loads(line)}
                        return
        return
    if path.suffix.lower() == '.txt':
        with path.open(encoding='utf-8-sig') as stream:
            for line in stream:
                if line.strip():
                    yield {'raw_line':line.rstrip('\r\n'),'columns':line.rstrip('\r\n').split('\t')}
        return
    if path.suffix.lower() == '.csv':
        with path.open(encoding='utf-8-sig', newline='') as stream:
            first_line=stream.readline();stream.seek(0)
            yield from csv.DictReader(stream,delimiter='\t' if '\t' in first_line else ',')
        return
    text = path.read_text(encoding='utf-8-sig')
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        for number, line in enumerate(text.splitlines(), 1):
            if line.strip():
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f'{path.name} 第{number}行不是合法JSON') from exc
    else:
        if isinstance(obj, list):
            yield from obj
        else:
            yield obj


def check_download(body, filename):
    # 防止把登录页、拒绝访问页或LFS指针误记为成功下载的数据。
    beginning = body[:512].lstrip().lower()
    if beginning.startswith((b'<!doctype html', b'<html', b'version https://git-lfs')):
        raise ValueError('服务器返回HTML页面或Git LFS指针，不是真实数据。')
    if not body:
        raise ValueError('服务器返回空文件。')
    suffix = Path(filename).suffix.lower()
    if suffix == '.zip':
        with zipfile.ZipFile(io.BytesIO(body)) as archive:
            if archive.testzip() is not None:
                raise ValueError('ZIP校验失败。')
    if suffix in {'.json', '.jsonl'}:
        text = body.decode('utf-8-sig')
        try:
            json.loads(text)
        except json.JSONDecodeError:
            for line in text.splitlines():
                if line.strip():
                    json.loads(line)


def fetch(row):
    if not row['assets']:
        raise ValueError(f"{row['name']} 没有已核实的自动下载文件；状态={row['access_status']}。请查看该目录README的作者入口。")
    log_path = ROOT / 'data' / 'download-log.json'
    log = read_json(log_path) if log_path.exists() else []
    failed = 0
    for asset in sorted(row['assets'],key=lambda item:bool(item.get('archive_member'))):
        path = safe_path(asset['path'])
        try:
            # bundled文件有固定SHA-256，存在时直接校验，不反复下载。
            expected = asset.get('sha256')
            if path.exists() and expected and hashlib.sha256(path.read_bytes()).hexdigest() == expected:
                print(f'已校验 {asset["path"]}')
                continue
            if asset.get('generated_content') is not None:
                body=asset['generated_content'].encode('utf-8')
            elif asset.get('archive_member'):
                archive_name=asset['source_archive']
                local=next((safe_path(a['path']) for a in row['assets'] if Path(a['path']).name==archive_name),None)
                if local is None or not local.exists():
                    restore_archives(row)
                    local=ROOT/'datasets'/row['id']/'raw'/archive_name
                if not local.exists():
                    raise ValueError('缺少完整源归档；先恢复对应归档，再提取成员。')
                with zipfile.ZipFile(local) as archive:
                    body=archive.read(asset['archive_member'])
            else:
                headers={'User-Agent':'Dataset4EventSchema/1.0'}
                if asset.get('http_range'):
                    start,end=asset['http_range'];headers['Range']=f'bytes={start}-{end}'
                req=urllib.request.Request(asset['url'],headers=headers)
                with urllib.request.urlopen(req,timeout=60) as response:
                    if asset.get('http_range'):
                        expected_range=f'bytes {start}-{end}/'
                        if response.status!=206 or not response.headers.get('Content-Range','').startswith(expected_range):
                            raise ValueError('下载服务器未返回所请求的字节范围；未保存伪分片。')
                    body=response.read(100*1024*1024+1)
                if len(body)>100*1024*1024:
                    raise ValueError('文件超过GitHub单文件限制；请使用分片归档。')
            check_download(body, path.name)
            digest = hashlib.sha256(body).hexdigest()
            if expected and digest != expected:
                raise ValueError('SHA-256与已登记文件不一致；未覆盖现有文件。')
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_suffix(path.suffix + '.part')
            temporary.write_bytes(body)
            temporary.replace(path)
            log.append({'dataset_id':row['id'],'url':asset['url'],'path':asset['path'],'sha256':digest,'bytes':len(body),'downloaded_at':dt.datetime.now(dt.timezone.utc).isoformat()})
            print(f'已下载 {asset["path"]} ({len(body)} bytes) SHA-256={digest}')
        except (OSError, ValueError) as exc:
            failed += 1
            print(f'下载失败 {asset["url"]}: {exc}', file=sys.stderr)
    log_path.parent.mkdir(exist_ok=True)
    log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
    return 1 if failed else 0


def restore_archives(row):
    """按已提交的分片和校验清单合并原始归档，输出到不提交Git的raw目录。"""
    folder=ROOT/'datasets'/row['id']
    manifests=sorted((folder/'data').rglob('*.manifest.json'))
    if not manifests:
        raise ValueError('该数据集不需要合并分片；完整文件已位于data目录。')
    for path in manifests:
        manifest=read_json(path)
        name=Path(manifest['original_filename']).name
        target=folder/'raw'/name;target.parent.mkdir(parents=True,exist_ok=True)
        temporary=target.with_suffix(target.suffix+'.part')
        total=0;whole=hashlib.sha256()
        with temporary.open('wb') as output:
            for part in manifest['parts']:
                source=(path.parent/part['file']).resolve()
                if not source.is_relative_to(path.parent.resolve()):
                    raise ValueError('分片路径越过数据目录。')
                digest=hashlib.sha256();size=0
                with source.open('rb') as stream:
                    while block:=stream.read(1024*1024):
                        output.write(block);digest.update(block);whole.update(block);size+=len(block)
                if size!=part['bytes'] or digest.hexdigest()!=part['sha256']:
                    raise ValueError(f'分片校验失败：{part["file"]}')
                total+=size
        if total!=manifest['original_bytes'] or whole.hexdigest()!=manifest['sha256']:
            raise ValueError('合并文件整体校验失败。')
        temporary.replace(target)
        print(f'已恢复 {target.relative_to(ROOT).as_posix()} ({total} bytes)，整体SHA-256校验通过。')


def validate():
    errors = []
    data = catalog()
    identifiers = [r['id'] for r in data]
    if len(set(identifiers)) != len(identifiers):
        errors.append('目录ID重复')
    actual_dirs = {p.name for p in (ROOT/'datasets').iterdir() if p.is_dir()}
    if actual_dirs != set(identifiers):
        errors.append('目录与catalog不一致')
    for row in data:
        folder = ROOT/'datasets'/row['id']
        try:
            metadata = read_json(folder/'metadata.json')
            if metadata != row:
                errors.append(f'{row["id"]}: metadata与catalog不一致')
            if not (folder/'README.md').is_file():
                errors.append(f'{row["id"]}: 缺少README')
            example = read_json(safe_path(row['example_path']))
            note = example['_说明']
            if note['kind'] != row['example_kind'] or note['is_official_sample'] != (row['example_kind']=='upstream_record'):
                errors.append(f'{row["id"]}: 真实/模板标识不一致')
            if not note['字段注释'] or not example['record']:
                errors.append(f'{row["id"]}: 缺少字段注释或示例')
            if row['example_kind']=='upstream_record' and not note.get('provenance'):
                errors.append(f'{row["id"]}: 真实样本缺少来源')
            record = example['record']
            if row['id']=='odin':
                ids={e['@id'] for e in record['events']}
                for event in record['events']:
                    for target in event.get('children',[])+event.get('outlinks',[]):
                        if target not in ids:
                            errors.append(f'odin: 悬空节点引用 {target}')
            if row['id']=='openepbench' and record['question_record']['id'] != record['answer_record']['id']:
                errors.append('openepbench: 问答样例ID不匹配')
            if row['category']=='event_generalization':
                # 同时核验完整CSV、info表和真实样例，防止版本统计及样例漂移。
                samples=list(records(safe_path(row['assets'][0]['path'])))
                info=list(records(safe_path(row['assets'][1]['path'])))
                stats=row['statistics']
                counts=Counter(item['abstract_event'] for item in samples)
                if len(samples)!=stats['records'] or len(counts)!=stats['classes']:
                    errors.append(f'{row["id"]}: 样本数或类别数与登记不一致')
                if list(samples[0])!=stats['fields'] or record!=samples[0]:
                    errors.append(f'{row["id"]}: CSV字段或真实样例不一致')
                if len(info)!=len(counts) or {i['abstract_event'] for i in info}!=set(counts):
                    errors.append(f'{row["id"]}: info候选类别与样本类别不一致')
                for item in info:
                    label=item['abstract_event']
                    if counts[label]!=int(item[stats['info_count_column']]):
                        errors.append(f'{row["id"]}: {label}的样本计数错误')
                    if 'trigger_count' in item:
                        distinct={r['trigger'] for r in samples if r['abstract_event']==label}
                        if len(distinct)!=int(item['trigger_count']):
                            errors.append(f'{row["id"]}: {label}的触发词计数错误')
                if 'trigger_offset' in stats['fields']:
                    for item in samples:
                        offset=json.loads(item['trigger_offset'])
                        if not (isinstance(offset,list) and len(offset)==2 and all(type(x) is int for x in offset) and 0<=offset[0]<offset[1]):
                            errors.append(f'{row["id"]}: 非法的触发词token跨度')
            # 检查自编抽取样例中提及和字符跨度确实一致。
            if row['example_kind']=='illustrative_template' and 'text' in record:
                for event in record.get('events',[]):
                    if 'character_span' in event:
                        start,end=event['character_span']
                        if record['text'][start:end] != event['mention']:
                            errors.append(f'{row["id"]}: mention跨度不匹配')
            for asset in row['assets']:
                path=safe_path(asset['path'])
                if asset.get('bundled'):
                    if not path.is_file():
                        errors.append(f'缺少随附数据 {asset["path"]}')
                    elif hashlib.sha256(path.read_bytes()).hexdigest()!=asset['sha256']:
                        errors.append(f'随附数据哈希不一致 {asset["path"]}')
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f'{row["id"]}: {exc}')
    if errors:
        print('\n'.join(errors),file=sys.stderr)
        return 1
    print(f'通过：{len(data)}个资源目录，元数据、示例来源、字段注释、图引用、问答配对、字符跨度及随附文件哈希均一致。')
    return 0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest='command',required=True)
    commands.add_parser('list');commands.add_parser('validate')
    for name in ['show','fetch','inspect','restore']:
        p=commands.add_parser(name);p.add_argument('dataset_id')
    args=parser.parse_args()
    try:
        if args.command=='list':
            for row in catalog():
                print(f"{row['id']:<28} {row['name']} [{row['access_status']}]")
        elif args.command=='validate':
            return validate()
        else:
            row=choose(args.dataset_id)
            if args.command=='show':
                print(json.dumps(read_json(safe_path(row['example_path'])),ensure_ascii=False,indent=2))
            elif args.command=='fetch':
                return fetch(row)
            elif args.command=='restore':
                restore_archives(row)
            else:
                found=False
                for asset in row['assets']:
                    if asset.get('storage') in {'multipart','manifest'}:
                        continue
                    path=safe_path(asset['path'])
                    if path.name.lower().startswith(('readme','license')) or path.suffix.lower() in {'.md','.pptx'}:
                        continue
                    if path.exists():
                        found=True
                        print(f'文件：{asset["path"]}')
                        print(json.dumps(next(records(path)),ensure_ascii=False,indent=2))
                        break
                if not found:
                    candidates=list((ROOT/'datasets'/row['id']/'raw').glob('*'))
                    usable=[p for p in candidates if p.is_file() and p.suffix in {'.gz','.zip'}]
                    if usable:
                        print(json.dumps(next(records(usable[0])),ensure_ascii=False,indent=2))
                    else:
                        raise ValueError('没有可直接查看的完整文件；分片数据先运行 restore，其他数据运行 fetch。')
    except (OSError, ValueError, StopIteration, KeyError) as exc:
        print(f'错误：{exc}',file=sys.stderr)
        return 1
    return 0


if __name__=='__main__':
    raise SystemExit(main())
