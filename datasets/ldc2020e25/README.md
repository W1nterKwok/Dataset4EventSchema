# LDC2020E25

> 当前下载状态：**partial**。已保存作者公开的156个LDC来源派生事件图，保留train/dev/test目录。 这些是公开派生图，不是LDC2020E25原始授权文本；原始LDC语料未取得。 详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


LDC模式学习语料及论文派生复杂事件图。

## 用途与版本

- 研究用途：复杂图结构、补全及预测。
- 固定版本：LDC2020E25；派生8/12节点图另列版本
- 获取状态：`partial_download`
- 数据许可：LDC 授权条款，未获取原始数据

先确认 LDC 访问资格和授权；派生样本数不是原始文档数。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show ldc2020e25
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch ldc2020e25` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- **当前已取得派生事件图的来源论文**：[The Future is not One-dimensional: Complex Event Schema Induction by Graph Modeling for Event Prediction](https://aclanthology.org/2021.emnlp-main.422/)（Manling Li 等，EMNLP 2021）。
- **本项目参考的后续使用论文**：[ReST-Pre: Event prediction by spatial-temporal structural replay on generative implicit event pattern induction](https://doi.org/10.1016/j.eswa.2025.130461)（Kai Huang 等，Expert Systems with Applications，2026）。
- **版本说明**：当前保存的是作者公开的派生事件图，不是 LDC2020E25 完整授权语料；以上论文用于说明图数据及实验来源。

- https://www.ldc.upenn.edu/
- https://github.com/snowfalling77/ReST-Pre

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
