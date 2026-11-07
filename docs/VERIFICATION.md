# 来源核验与获取记录

核验日期：2026-11-07。本记录区分“作者报告”“本地已取得”和“尚未取得”。

| 资源 | 核验结果 | 当前处理 |
| --- | --- | --- |
| ODIN | 作者GitHub仓库含18个 `odin_curated` JSON；GPL-3.0 | 随仓库提供全部18个模式、完整许可证、SHA-256；真实示例保留完整图以免节点引用断裂 |
| OpenEPBench | 作者GitHub仓库含中英文验证数据及问题/答案样本；MIT | 随仓库提供四个文件、完整许可证；真实示例按id配对；注意`.json`文件实际采用JSONL |
| proScript | 作者主页可下载 `proscript_v1a.zip` | 可通过fetch下载至raw；原始全集与论文1子集不等同；数据再分发许可未独立核实 |
| EV² | 作者GitHub四个任务JSONL均下载成功 | 本地raw中保存，固定commit及SHA-256；未在上游发现独立数据许可证，不随Git发布 |
| MATRES | 作者关系标签文件为aquaint.txt、platinum.txt、timebank.txt | 获取三组关系标注，需自行取得配套原文；不把rawdata里的分析CSV当主标注 |
| RESIN-11 | ReST-Pre公开有resin-schemalib.json；inc-schema的phase2a是提示章节 | 仅提供候选库下载；尚未确认RESIN-11的确切场景与评测映射，不冒充已完成金标准整合 |
| IED / LDC | ReST-Pre README画出原始和派生文件，但其Git树只实际提供RESIN库和本体等 | 保留原始项目入口和获取限制，不依据README目录树宣称文件已发布或已下载 |
| MAVEN/ESC-CGEP及AECR | 论文提供anonymous.4open.science/r/AECR-AFAF；根README可读，子目录API在本环境返回401 | 保留作者入口；文件覆盖、真实字段和许可仍需核实 |
| GDELT/ICEWS（LAMP） | 作者README提供固定Google Drive数据包 | 保留指定版本及下载入口，不用其他年份替代 |
| MIRAI / GDELT-500（论文10） | 已核实原始MIRAI仓库；尚未核实论文10改造版本发布位置 | 明确版本待核实，不把原版当作论文10的同一查询集 |
| RESPONSE | DataCite DOI元数据确认v1、作者及CC-BY-NC-SA-4.0；UCL/Figshare下载返回403 | 固定论文及数据DOI，示例为自编模板，原始数据尚未下载 |
| HiEve | ACL Anthology核实文本事件层级论文L14-1020 | 继续标记原始下载地址待核实，排除同名视频集 |
| SchemaAug / EECKG / 自建语料 | 分别核实论文入口、所引资源语境，或拟建状态 | 给出独立目录、中文任务说明和自编格式示例，不声明已获取原始语料 |

GitHub公开仓库中未标明数据许可，不意味着可以重新授权。代码许可不自动覆盖第三方新闻和原始语料。下载的raw与日志均默认不提交。

## 核验命令

```bash
python scripts/datasets.py validate
python scripts/datasets.py fetch ev2
python scripts/datasets.py fetch matres
python scripts/datasets.py fetch proscript
```

自动验证覆盖目录一致性、示例来源标识、中文注释、真实模式引用、问答配对、示例字符跨度、随附数据哈希。下载器拒绝HTML错误页和Git LFS指针，并为实际下载记录时间和SHA-256。
