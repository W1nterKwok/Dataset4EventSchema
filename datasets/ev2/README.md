# EV² / EV2

> 当前下载状态：**downloaded**。四个完整任务JSONL及clustering.json。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


模式层、实例层的CEC与CRR多关系推理基准。

## 用途与版本

- 研究用途：分别评价模式知识和实例关系推理。
- 固定版本：四个官方 JSONL 文件 @ 41dc03061fa2658ac57f75664e484e1a8e625f35
- 获取状态：`bundled`
- 数据许可：未核实数据许可

S_CEC、I_CEC、S_CRR、I_CRR 分项报告；下载不等于获得再分发许可。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show ev2
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

python scripts/datasets.py fetch ev2

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://github.com/TZWwww/EV2

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
