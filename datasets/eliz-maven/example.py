"""读取首条真实样本，分开展示模型输入和评测标注；无需模型或API密钥。"""
import csv
import json
from pathlib import Path


def main():
    data = Path(__file__).resolve().parent / 'data'
    with (data / 'Eliz-MAVEN.csv').open(encoding='utf-8-sig', newline='') as stream:
        row = next(csv.DictReader(stream))
    with (data / 'Eliz-MAVEN_info.csv').open(encoding='utf-8-sig', newline='') as stream:
        candidates = [item['abstract_event'] for item in csv.DictReader(stream)]
    # 候选类别来自官方info表；abstract_event是答案，不能作为模型提示的一部分。
    model_input = {'specific_event': row['specific_event'], 'candidate_labels': candidates}
    annotation = {'abstract_event': row['abstract_event']}

    # 偏移基于原始MAVEN tokens；这里只解析，不能对specific_event按字符或空格切片。
    annotation['trigger'] = row['trigger']
    annotation['trigger_offset_tokens'] = json.loads(row['trigger_offset'])

    print(json.dumps({'model_input': model_input, 'evaluation_only': annotation}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
