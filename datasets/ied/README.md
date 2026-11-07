# IED 新闻实例图

> 当前下载状态：**downloaded**。作者完整Wiki_IED_split.tgz及六个Wikipedia原文压缩包；未声称等同于论文2的三类清洗子集。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


IED主题的事件与实体实例图。

## 用途与版本

- 研究用途：实例图到模式图的归纳及预测。
- 固定版本：论文2清洗版与 ReST-Pre 派生版必须分别固定
- 获取状态：`bundled`
- 数据许可：未核实数据许可

ReST-Pre README 的目录树列出数据，不代表其 Git 树实际包含该数据；不得混用两版图数。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show ied
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch ied` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://github.com/limanling/temporal-graph-schema
- https://github.com/snowfalling77/ReST-Pre

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
