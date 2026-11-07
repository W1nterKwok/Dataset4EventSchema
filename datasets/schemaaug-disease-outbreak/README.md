# SchemaAug / Disease Outbreak

> 当前下载状态：**partial**。已保存对应RESIN公开事件模式JSON，作为数据增强的辅助资源。 尚未找到可验证的SchemaAug场景新闻及原始抽取标注发布包；辅助模式不是新闻语料。 详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


SchemaAug低资源新闻抽取场景子集。

## 用途与版本

- 研究用途：模式引导的数据增强和上游事件抽取。
- 固定版本：论文2/SchemaAug中的disease outbreak子集
- 获取状态：`partial_download`
- 数据许可：未核实数据许可

原始新闻及标注的发布和权限待核实；增强样本仅进入训练集，不能当作未来事件预测金标准。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show schemaaug-disease-outbreak
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch schemaaug-disease-outbreak` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- **SchemaAug 实验数据对应论文**：[Schema-based Data Augmentation for Event Extraction](https://aclanthology.org/2024.lrec-main.1253/)（Xiaomeng Jin、Heng Ji，LREC-COLING 2024）。
- **本项目参考的学位论文**：[Knowledge-aware data generation](https://hdl.handle.net/2142/129847)（Xiaomeng Jin，University of Illinois Urbana-Champaign 博士学位论文，2025，第 3 章）。
- **当前已取得辅助模式库的来源论文**：[RESIN-11: Schema-guided Event Prediction for 11 Newsworthy Scenarios](https://aclanthology.org/2022.naacl-demo.7/)（Xinya Du 等，NAACL 2022 System Demonstrations）。
- **版本说明**：当前仅保存 RESIN 辅助模式 JSON，尚未取得该场景完整的 SchemaAug 新闻语料；辅助模式库与论文中的新闻样本应分开引用。

- https://aclanthology.org/2024.lrec-main.1253/

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
