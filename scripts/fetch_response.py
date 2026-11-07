"""从官方Figshare接口取得固定v1的RESPONSE文件；不接受HTML错误页。"""
from pathlib import Path
import argparse
import hashlib
import json
import urllib.request


def get(url):
    request=urllib.request.Request(url,headers={'User-Agent':'Dataset4EventSchema/1.0 (research data download)'})
    with urllib.request.urlopen(request,timeout=60) as response:
        return response.read()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    url='https://api.figshare.com/v2/articles/26010064/versions/1'
    metadata=json.loads(get(url))
    if metadata.get('doi')!='10.5522/04/26010064.v1':
        raise ValueError('接口未返回所需DOI v1；停止下载。')
    files=metadata.get('files',[])
    if not files:
        raise ValueError('官方v1元数据没有可下载文件。')
    manifest=[]
    for asset in files:
        filename=Path(asset['name']).name
        if filename!=asset['name']:
            raise ValueError('不安全的官方文件路径。')
        body=get(asset['download_url'])
        if body[:512].lstrip().lower().startswith((b'<html',b'<!doctype html')):
            raise ValueError('下载地址返回HTML，未写入数据。')
        if asset.get('size') and len(body)!=asset['size']:
            raise ValueError('数据长度与官方元数据不一致。')
        expected=asset.get('computed_md5') or asset.get('supplied_md5')
        if expected and hashlib.md5(body).hexdigest()!=expected:
            raise ValueError('数据MD5与官方元数据不一致。')
        (args.output/filename).write_bytes(body)
        manifest.append({'name':filename,'url':asset['download_url'],'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest(),'official_md5':expected})
        print(filename,len(body),'bytes')
    (args.output/'official-metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
    (args.output/'download-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')


if __name__=='__main__':
    main()
