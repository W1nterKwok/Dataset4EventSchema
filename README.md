# Dataset4EventSchema

事件模式归纳、事件关系抽取、事件预测与危机场景推理的数据集索引、带中文注释的示例及获取工具。共整理 **27 个独立资源目录**

已将可取得的原始数据保存到各目录的`data/`并上传GitHub：16项公开发布文件已取得，10项为部分/派生/辅助数据，另1项拟自建。逐项范围见[下载清单](docs/DOWNLOADS.md)；不把辅助文件或示例计作完整原始语料。

## 快速使用

只依赖 Python 3.10+ 标准库，无API密钥。

```bash
python scripts/datasets.py list
python scripts/datasets.py show response
python scripts/datasets.py validate
python scripts/datasets.py fetch ev2
python scripts/datasets.py inspect ev2
python datasets/eliz-maven/example.py
python scripts/datasets.py restore conceptnet
python scripts/datasets.py restore mirai
```

`fetch`只下载已登记的文件，固定作者提交，保存哈希及时间。`inspect`读取本地原始JSON/JSONL/CSV并展示首条记录。没有已核实自动下载地址的资源会返回明确状态，不会生成假数据。Windows可用 `py -3` 代替 `python`。

## 数据集目录

| 数据集 | 任务类别 | 下载状态 | 示例来源 |
| --- | --- | --- | --- |
| [RESIN-11](datasets/resin-11/) | schema_induction | `partial` | 自编格式示例 |
| [ODIN](datasets/odin/) | schema_induction | `downloaded` | 作者真实记录 |
| [proScript](datasets/proscript/) | schema_induction | `downloaded` | 自编格式示例 |
| [IED 新闻实例图](datasets/ied/) | instance_graph | `downloaded` | 自编格式示例 |
| [LDC2020E25](datasets/ldc2020e25/) | instance_graph | `partial` | 自编格式示例 |
| [MAVEN-CGEP](datasets/maven-cgep/) | causal_prediction | `partial` | 自编格式示例 |
| [ESC-CGEP](datasets/esc-cgep/) | causal_prediction | `partial` | 自编格式示例 |
| [MAVEN-AECR](datasets/maven-aecr/) | abstract_rules | `downloaded` | 自编格式示例 |
| [EV² / EV2](datasets/ev2/) | event_reasoning | `downloaded` | 自编格式示例 |
| [GDELT（LAMP版本）](datasets/gdelt-lamp/) | structured_prediction | `downloaded` | 自编格式示例 |
| [MIRAI（论文10设置）](datasets/mirai/) | text_prediction | `partial` | 自编格式示例 |
| [OpenEPBench](datasets/openepbench/) | open_ended_prediction | `downloaded` | 作者真实记录 |
| [SchemaAug / Kidnapping](datasets/schemaaug-kidnapping/) | extraction_augmentation | `partial` | 自编格式示例 |
| [SchemaAug / Ukraine Crisis](datasets/schemaaug-ukraine-crisis/) | extraction_augmentation | `partial` | 自编格式示例 |
| [SchemaAug / Mass Shooting](datasets/schemaaug-mass-shooting/) | extraction_augmentation | `partial` | 自编格式示例 |
| [SchemaAug / Disease Outbreak](datasets/schemaaug-disease-outbreak/) | extraction_augmentation | `partial` | 自编格式示例 |
| [SchemaAug / WCEP](datasets/schemaaug-wcep/) | extraction_augmentation | `partial` | 自编格式示例 |
| [ConceptNet](datasets/conceptnet/) | commonsense_knowledge | `downloaded` | 自编格式示例 |
| [ECCKG（原清单记作EECKG）](datasets/eeckg/) | commonsense_knowledge | `downloaded` | 自编格式示例 |
| [自建网络暴力事件语料（待建设）](datasets/cyberbullying-local/) | custom_corpus | `planned` | 自编格式示例 |
| [MAVEN-ERE](datasets/maven-ere/) | relation_extraction | `downloaded` | 自编格式示例 |
| [MATRES](datasets/matres/) | relation_extraction | `downloaded` | 自编格式示例 |
| [HiEve（文本事件层级）](datasets/hieve/) | relation_extraction | `downloaded` | 自编格式示例 |
| [EventStoryLine / ESC](datasets/eventstoryline/) | relation_extraction | `downloaded` | 自编格式示例 |
| [RESPONSE](datasets/response/) | crisis_reasoning | `downloaded` | 作者真实记录 |
| [Eliz-EV²](datasets/eliz-ev2/) | event_generalization | `downloaded` | 作者真实记录 |
| [Eliz-MAVEN](datasets/eliz-maven/) | event_generalization | `downloaded` | 作者真实记录 |

## 目录约定

```text
catalog.json                  # 全部资源、来源、版本和获取状态
datasets/<id>/README.md        # 数据简介、项目用途、获取方式
datasets/<id>/metadata.json    # 单项机器可读元数据
datasets/<id>/example.json     # 示例及中文字段注释
datasets/<id>/data/            # 已归档的数据、原始压缩包或分片
datasets/<id>/raw/             # 大归档合并输出和临时文件，不提交Git
scripts/datasets.py            # 目录查询、下载、原始样本查看与验证
```

合并条目已拆开：MAVEN-AECR、ConceptNet/ECCKG和五种SchemaAug新闻子集分别建目录。正文提到的MAVEN-ERE、MATRES、HiEve、EventStoryLine也单列；拟自建网络暴力语料标记 `planned`。

## 实际文件与仍有的缺口

- RESPONSE官方两个JSON已下载并校验，取代此前403状态；保留论文统计与发布文件统计的区别。
- ConceptNet和MIRAI完整发布归档采用分片保存，运行`restore conceptnet`或`restore mirai`合并并校验。
- IED、MAVEN-ERE、EV²、MATRES、proScript、ECCKG、GDELT、HiEve等已保存本次取得的公开文件；具体范围以每项DOWNLOAD_STATUS为准。
- SchemaAug仅找到辅助模式；LDC仅取得公开派生图；部分CGEP文件和论文10筛选版本仍待补齐。
- 拟自建语料保留为项目模板，尚无现成下载包。

详见[示例格式](docs/FORMAT.md)、[评测约定](docs/EVALUATION.md)、[许可说明](LICENSE-NOTICE.md)和[核验记录](docs/VERIFICATION.md)。整理日期：2026-11-07。
