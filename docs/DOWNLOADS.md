# 原始数据下载与缺口

更新时间：2026-11-07。30个目录逐项核查：**16项已取得确认的公开发布文件，10项取得部分/派生/辅助数据，3项尚未取得指定版本，1项为拟自建语料**。实际保存文件总字节数为2,044,699,745，大文件分片和提取表可能包含同源重复内容。

| 数据集 | 状态 | 实际文件数 | 已保存范围及缺口 |
| --- | --- | --- | --- |
| [RESIN-11](../datasets/resin-11/DOWNLOAD_STATUS.md) | `partial` | 30 | 已保存RESIN-KAIROS官方模式库的17个JSON和11个可视化PPTX，以及旧版10模式参考库。 论文1的11场景评测映射及节点/边统计尚未逐项对齐；旧10模式库不冒充RESIN-11金标准。 |
| [ODIN](../datasets/odin/DOWNLOAD_STATUS.md) | `downloaded` | 18 | 作者已公开且此前随仓库保存的数据文件。  |
| [proScript](../datasets/proscript/DOWNLOAD_STATUS.md) | `downloaded` | 1 | 作者完整proscript_v1a.zip（train/dev/test）。  |
| [IED 新闻实例图](../datasets/ied/DOWNLOAD_STATUS.md) | `downloaded` | 7 | 作者完整Wiki_IED_split.tgz及六个Wikipedia原文压缩包；未声称等同于论文2的三类清洗子集。  |
| [LDC2020E25](../datasets/ldc2020e25/DOWNLOAD_STATUS.md) | `partial` | 156 | 已保存作者公开的156个LDC来源派生事件图，保留train/dev/test目录。 这些是公开派生图，不是LDC2020E25原始授权文本；原始LDC语料未取得。 |
| [MAVEN-CGEP](../datasets/maven-cgep/DOWNLOAD_STATUS.md) | `partial` | 4 | 已保存AECR作者项目公开的事件词典及事件映射等辅助文件。 未取得完整MAVEN-CGEP图、候选集与划分文件；SeDGPL加载器所需MAVENSubWoRe.npy不在其公开树中。 |
| [ESC-CGEP](../datasets/esc-cgep/DOWNLOAD_STATUS.md) | `partial` | 3 | 已保存SeDGPL作者发布的ESCSubWoRe.npy及事件词典/映射。 已验证NumPy文件头，未执行对象反序列化；尚未确认其全部样本/候选与AECR论文采用版本完全一致。 |
| [MAVEN-AECR](../datasets/maven-aecr/DOWNLOAD_STATUS.md) | `downloaded` | 11 | 作者公开733条抽象规则、规则映射、聚类输出及检索训练配对文件；保留作者命名。  |
| [ESC-AECR](../datasets/esc-aecr/DOWNLOAD_STATUS.md) | `unavailable` | 0 | 没有取得所请求版本的真实数据文件。 作者匿名项目公开的是733条MAVEN规则及关联数据，未找到ESC的180条规则发布文件。 |
| [EV² / EV2](../datasets/ev2/DOWNLOAD_STATUS.md) | `downloaded` | 5 | 四个完整任务JSONL及clustering.json。  |
| [GDELT（LAMP版本）](../datasets/gdelt-lamp/DOWNLOAD_STATUS.md) | `downloaded` | 3 | 作者包中的gdelt.pkl及entity_map.pkl，并保留完整LAMP数据发布包。没有执行pickle反序列化。  |
| [ICEWS（LAMP版本）](../datasets/icews-lamp/DOWNLOAD_STATUS.md) | `unavailable` | 0 | 没有取得所请求版本的真实数据文件。 已下载并检查作者指定Google Drive包，实际仅含GDELT与Amazon文件，没有ICEWS；未发现可核实的该论文时间范围预处理发布包。 |
| [MIRAI（论文10设置）](../datasets/mirai/DOWNLOAD_STATUS.md) | `partial` | 10 | 已保存完整MIRAI官方发布包（581,967,516字节，7片），另提取705条测试查询和100条子集查询。 原始包实测296,630条新闻、589,930条历史KG记录；不直接声称等同于论文10所列152,500历史事件的筛选版本。 |
| [GDELT-500（论文10改造版）](../datasets/gdelt-500/DOWNLOAD_STATUS.md) | `unavailable` | 0 | 没有取得所请求版本的真实数据文件。 未定位论文10所用420查询、189,743新闻、119,388历史事件的改造版本发布位置，不以其他同名数据替代。 |
| [OpenEPBench](../datasets/openepbench/DOWNLOAD_STATUS.md) | `downloaded` | 4 | 作者已公开且此前随仓库保存的数据文件。  |
| [SchemaAug / Kidnapping](../datasets/schemaaug-kidnapping/DOWNLOAD_STATUS.md) | `partial` | 1 | 已保存对应RESIN公开事件模式JSON，作为数据增强的辅助资源。 尚未找到可验证的SchemaAug场景新闻及原始抽取标注发布包；辅助模式不是新闻语料。 |
| [SchemaAug / Ukraine Crisis](../datasets/schemaaug-ukraine-crisis/DOWNLOAD_STATUS.md) | `partial` | 1 | 已保存对应RESIN公开事件模式JSON，作为数据增强的辅助资源。 尚未找到可验证的SchemaAug场景新闻及原始抽取标注发布包；辅助模式不是新闻语料。 |
| [SchemaAug / Mass Shooting](../datasets/schemaaug-mass-shooting/DOWNLOAD_STATUS.md) | `partial` | 1 | 已保存对应RESIN公开事件模式JSON，作为数据增强的辅助资源。 尚未找到可验证的SchemaAug场景新闻及原始抽取标注发布包；辅助模式不是新闻语料。 |
| [SchemaAug / Disease Outbreak](../datasets/schemaaug-disease-outbreak/DOWNLOAD_STATUS.md) | `partial` | 1 | 已保存对应RESIN公开事件模式JSON，作为数据增强的辅助资源。 尚未找到可验证的SchemaAug场景新闻及原始抽取标注发布包；辅助模式不是新闻语料。 |
| [SchemaAug / WCEP](../datasets/schemaaug-wcep/DOWNLOAD_STATUS.md) | `partial` | 1 | 已保存对应RESIN公开事件模式JSON，作为数据增强的辅助资源。 尚未找到可验证的SchemaAug场景新闻及原始抽取标注发布包；辅助模式不是新闻语料。 |
| [ConceptNet](../datasets/conceptnet/DOWNLOAD_STATUS.md) | `downloaded` | 7 | ConceptNet 5.7.0完整多语言断言CSV.gz（497,963,447字节，6片），不是英语抽样。  |
| [ECCKG（原清单记作EECKG）](../datasets/eeckg/DOWNLOAD_STATUS.md) | `downloaded` | 5 | ECCKG作者Zenodo v1全部五个文件；逐文件MD5与Zenodo官方记录一致。  |
| [自建网络暴力事件语料（待建设）](../datasets/cyberbullying-local/DOWNLOAD_STATUS.md) | `planned` | 0 | 项目拟自建语料，没有可下载的现成数据。 尚未采集和标注，不创建伪原始数据。 |
| [MAVEN-ERE](../datasets/maven-ere/DOWNLOAD_STATUS.md) | `downloaded` | 1 | 官方v1.0完整ZIP：train 2,913、valid 710、test 857篇；官方测试金标本身不公开。  |
| [MATRES](../datasets/matres/DOWNLOAD_STATUS.md) | `downloaded` | 3 | 作者发布的aquaint、platinum、timebank三份完整关系标注；不包含另行授权的配套新闻原文。  |
| [HiEve（文本事件层级）](../datasets/hieve/DOWNLOAD_STATUS.md) | `downloaded` | 401 | 公开清洗版hievents_v2全部文件，含100篇processed文档与上游提供的特征文件；原始RAR地址404。  |
| [EventStoryLine / ESC](../datasets/eventstoryline/DOWNLOAD_STATUS.md) | `downloaded` | 4697 | 作者公开annotated_data、evaluation_format、ECB+配套包及许可说明，保留多版本目录。  |
| [RESPONSE](../datasets/response/DOWNLOAD_STATUS.md) | `downloaded` | 3 | DOI v1官方发布的all_questions_v1.json、all_questions_v2.json及官方元数据；由GitHub下载任务取得并通过官方MD5。  |
| [Eliz-EV²](../datasets/eliz-ev2/DOWNLOAD_STATUS.md) | `downloaded` | 2 | 作者已公开且此前随仓库保存的数据文件。  |
| [Eliz-MAVEN](../datasets/eliz-maven/DOWNLOAD_STATUS.md) | `downloaded` | 2 | 作者已公开且此前随仓库保存的数据文件。  |

## 大归档恢复

ConceptNet保存完整5.7.0多语言断言文件的6个分片；MIRAI保存完整作者ZIP的7个分片。每片不超过80MiB。分片清单含各片SHA-256、顺序、原文件大小和整体SHA-256。

```bash
python scripts/datasets.py restore conceptnet
python scripts/datasets.py restore mirai
```

合并文件写入各自`raw/`目录（Git忽略）。对MIRAI提取ZIP即可得到作者的新闻、KG和查询表；705条及100条查询已另存于data/query_tables下。合并器逐片和整体校验后才发布最终文件。

## 下载核验

RESPONSE两个文件均从DOI v1官方API获取，MD5与官方元数据一致；本机403的问题通过GitHub运行环境成功解决。其发布文件分别为962和949条记录，不把两文件相加当作论文的1,789条已筛选实例，保留原样并注明口径差异。

ECCKG五个文件全部通过Zenodo官方MD5；GitHub来源固定提交和SHA-256；ConceptNet完整gzip通过解压CRC校验；MAVEN-ERE三个JSONL重新计数为2,913/710/857。仓库验证命令逐文件检查已提交资产的哈希。

`partial`表示已保存真实文件但仍有明确缺口。例如SchemaAug目录只有辅助事件模式，没有冒充新闻语料；LDC仅保存作者公开派生图；MIRAI保留完整原始发布包但未声称复现论文10的筛选版本。`unavailable`目录不放伪数据。
