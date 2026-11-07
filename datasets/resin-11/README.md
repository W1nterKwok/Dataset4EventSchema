# RESIN-11

> 当前下载状态：**partial**。已保存RESIN-KAIROS官方模式库的17个JSON和11个可视化PPTX，以及旧版10模式参考库。 论文1的11场景评测映射及节点/边统计尚未逐项对齐；旧10模式库不冒充RESIN-11金标准。 详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


11类新闻场景的时序及层级模式参考库。

## 用途与版本

- 研究用途：模式节点与时序、层级边归纳评测。
- 固定版本：RESIN-KAIROS官方公开模式库（17个JSON对应细分场景），附旧版10模式参考库
- 获取状态：`partial_download`
- 数据许可：未核实数据许可

inc-schema 的 phase2a 是章节提示，不是 RESIN-11 金标准；ReST-Pre 的 resin-schemalib.json 也不可直接认定为同一评测版本。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show resin-11
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

python scripts/datasets.py fetch resin-11

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- **数据集论文**：[RESIN-11: Schema-guided Event Prediction for 11 Newsworthy Scenarios](https://aclanthology.org/2022.naacl-demo.7/)（Xinya Du 等，NAACL 2022 System Demonstrations）。
- **本项目所参考的评测论文**：[Open-Domain Hierarchical Event Schema Induction by Incremental Prompting and Verification](https://aclanthology.org/2023.acl-long.312/)（Sha Li 等，ACL 2023）。
- **版本说明**：当前保存的是官方公开模式库及旧版参考库；与上述评测论文中 RESIN-11 金标准的场景映射尚未逐项核实。

- https://github.com/limanling/temporal-graph-schema
- https://github.com/raspberryice/inc-schema

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
