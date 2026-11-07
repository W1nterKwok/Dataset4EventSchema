# Dataset4EventSchema

事件模式归纳、事件关系抽取、事件预测与危机场景推理的数据集索引、带中文注释的示例及获取工具。共整理 **30 个独立资源目录**，包含 RESPONSE 和 ElizBench 的两个子集。

这个仓库整合数据入口、版本说明及示例；ODIN、OpenEP和ElizBench的两个公开子集已随仓库提供；其余数据依获取状态下载、申请或核实。每个示例都显式区分作者真实记录与自编格式示例。

## 快速使用

只依赖 Python 3.10+ 标准库，无API密钥。

```bash
python scripts/datasets.py list
python scripts/datasets.py show response
python scripts/datasets.py validate
python scripts/datasets.py fetch ev2
python scripts/datasets.py inspect ev2
python datasets/eliz-maven/example.py
```

`fetch`只下载已登记的文件，固定作者提交，保存哈希及时间。`inspect`读取本地原始JSON/JSONL/CSV并展示首条记录。没有已核实自动下载地址的资源会返回明确状态，不会生成假数据。Windows可用 `py -3` 代替 `python`。

## 数据集目录

| 数据集 | 任务类别 | 获取状态 | 示例来源 |
| --- | --- | --- | --- |
| [RESIN-11](datasets/resin-11/) | schema_induction | `version_verification_required` | 自编格式示例 |
| [ODIN](datasets/odin/) | schema_induction | `bundled` | 作者真实记录 |
| [proScript](datasets/proscript/) | schema_induction | `downloadable_license_unverified` | 自编格式示例 |
| [IED 新闻实例图](datasets/ied/) | instance_graph | `version_verification_required` | 自编格式示例 |
| [LDC2020E25](datasets/ldc2020e25/) | instance_graph | `restricted_access` | 自编格式示例 |
| [MAVEN-CGEP](datasets/maven-cgep/) | causal_prediction | `author_artifact_available` | 自编格式示例 |
| [ESC-CGEP](datasets/esc-cgep/) | causal_prediction | `author_artifact_available` | 自编格式示例 |
| [MAVEN-AECR](datasets/maven-aecr/) | abstract_rules | `author_artifact_available` | 自编格式示例 |
| [ESC-AECR](datasets/esc-aecr/) | abstract_rules | `author_artifact_available` | 自编格式示例 |
| [EV² / EV2](datasets/ev2/) | event_reasoning | `downloadable_license_unverified` | 自编格式示例 |
| [GDELT（LAMP版本）](datasets/gdelt-lamp/) | structured_prediction | `manual_acquisition` | 自编格式示例 |
| [ICEWS（LAMP版本）](datasets/icews-lamp/) | structured_prediction | `manual_acquisition` | 自编格式示例 |
| [MIRAI（论文10设置）](datasets/mirai/) | text_prediction | `version_verification_required` | 自编格式示例 |
| [GDELT-500（论文10改造版）](datasets/gdelt-500/) | text_prediction | `version_verification_required` | 自编格式示例 |
| [OpenEPBench](datasets/openepbench/) | open_ended_prediction | `bundled` | 作者真实记录 |
| [SchemaAug / Kidnapping](datasets/schemaaug-kidnapping/) | extraction_augmentation | `manual_acquisition` | 自编格式示例 |
| [SchemaAug / Ukraine Crisis](datasets/schemaaug-ukraine-crisis/) | extraction_augmentation | `manual_acquisition` | 自编格式示例 |
| [SchemaAug / Mass Shooting](datasets/schemaaug-mass-shooting/) | extraction_augmentation | `manual_acquisition` | 自编格式示例 |
| [SchemaAug / Disease Outbreak](datasets/schemaaug-disease-outbreak/) | extraction_augmentation | `manual_acquisition` | 自编格式示例 |
| [SchemaAug / WCEP](datasets/schemaaug-wcep/) | extraction_augmentation | `manual_acquisition` | 自编格式示例 |
| [ConceptNet](datasets/conceptnet/) | commonsense_knowledge | `manual_acquisition` | 自编格式示例 |
| [EECKG](datasets/eeckg/) | commonsense_knowledge | `source_verification_required` | 自编格式示例 |
| [自建网络暴力事件语料（待建设）](datasets/cyberbullying-local/) | custom_corpus | `planned` | 自编格式示例 |
| [MAVEN-ERE](datasets/maven-ere/) | relation_extraction | `manual_acquisition` | 自编格式示例 |
| [MATRES](datasets/matres/) | relation_extraction | `downloadable_license_unverified` | 自编格式示例 |
| [HiEve（文本事件层级）](datasets/hieve/) | relation_extraction | `source_verification_required` | 自编格式示例 |
| [EventStoryLine / ESC](datasets/eventstoryline/) | relation_extraction | `downloadable_license_unverified` | 自编格式示例 |
| [RESPONSE](datasets/response/) | crisis_reasoning | `download_blocked_403` | 自编格式示例 |
| [Eliz-EV²](datasets/eliz-ev2/) | event_generalization | `bundled` | 作者真实记录 |
| [Eliz-MAVEN](datasets/eliz-maven/) | event_generalization | `bundled` | 作者真实记录 |

## 目录约定

```text
catalog.json                  # 全部资源、来源、版本和获取状态
datasets/<id>/README.md        # 数据简介、项目用途、获取方式
datasets/<id>/metadata.json    # 单项机器可读元数据
datasets/<id>/example.json     # 示例及中文字段注释
datasets/<id>/data/            # 已核对许可的小规模随附资源
datasets/<id>/raw/             # 本地下载，默认不提交Git
scripts/datasets.py            # 目录查询、下载、原始样本查看与验证
```

合并条目已拆开：MAVEN/ESC-AECR、ConceptNet/EECKG和五种SchemaAug新闻子集分别建目录。正文提到的MAVEN-ERE、MATRES、HiEve、EventStoryLine也单列；拟自建网络暴力语料标记 `planned`。

## 版本和已知缺口

- RESIN章节提示不等于RESIN-11金标准，候选库下载后仍需核对评测子集。
- MAVEN/ESC-CGEP及AECR保留作者匿名发布入口；尚未确认该入口的可下载数据覆盖及许可。
- LAMP预处理的GDELT/ICEWS必须通过作者指定链接获取，不能替换为常见其他年份版本。
- 论文10的MIRAI及GDELT-500设置需额外核对；原始MIRAI入口不代表同一查询版本。
- RESPONSE固定 DOI v1，数据站在整理环境返回HTTP 403，当前保留入口和自编示例，未声称已下载。
- HiEve指文本事件层级资源，不是同名视频资源；原始来源尚待进一步核实。

ElizBench新增两个目录，含完整成品CSV、info统计表、真实样例和可运行的中文注释示例，详见[ElizBench说明](docs/ELIZBENCH.md)。

详见[示例格式](docs/FORMAT.md)、[评测约定](docs/EVALUATION.md)、[许可说明](LICENSE-NOTICE.md)和[核验记录](docs/VERIFICATION.md)。整理日期：2026-11-07。
