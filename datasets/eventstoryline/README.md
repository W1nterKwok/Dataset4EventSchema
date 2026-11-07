# EventStoryLine / ESC

> 当前下载状态：**downloaded**。作者公开annotated_data、evaluation_format、ECB+配套包及许可说明，保留多版本目录。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


新闻故事线的事件时间及因果标注。

## 用途与版本

- 研究用途：原始新闻事件关系抽取。
- 固定版本：作者公开版本；正式使用固定具体提交和语料版本
- 获取状态：`bundled`
- 数据许可：未核实数据许可

不同发布版和共指扩展预处理可能改变因果边数；ESC-CGEP是派生任务，不应混用。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show eventstoryline
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch eventstoryline` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://github.com/tommasoc80/EventStoryLine

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
