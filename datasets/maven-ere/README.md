# MAVEN-ERE

> 当前下载状态：**downloaded**。官方v1.0完整ZIP：train 2,913、valid 710、test 857篇；官方测试金标本身不公开。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


多种事件关系的文档级标注语料。

## 用途与版本

- 研究用途：原始文本中的事件关系抽取评测。
- 固定版本：原始MAVEN-ERE；固定作者划分
- 获取状态：`bundled`
- 数据许可：未核实数据许可

与 MAVEN-CGEP 和 MAVEN-AECR 分开管理；原始关系标签和token索引需按作者格式解析。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show maven-ere
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch maven-ere` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- **来源论文**：[MAVEN-ERE: A Unified Large-scale Dataset for Event Coreference, Temporal, Causal, and Subevent Relation Extraction](https://arxiv.org/abs/2211.07342)（Xiaozhi Wang 等，EMNLP 2022）。

- https://github.com/THU-KEG/MAVEN-ERE

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
