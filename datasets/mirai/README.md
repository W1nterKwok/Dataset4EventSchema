# MIRAI（论文10设置）

结构化历史事件与新闻文本结合的关系集合预测。

## 用途与版本

- 研究用途：新闻证据驱动的事件预测。
- 固定版本：Thinking Bidirectionally 使用的查询/筛选版本
- 获取状态：`version_verification_required`
- 数据许可：未核实数据许可

MIRAI 原始仓库是资源起点；未核实其与论文10所用705查询版本完全一致，不将原版统计直接套用到论文10。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show mirai
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

无已核实的自动下载资产；从下列作者入口获取并核对版本。

原始下载保存于 `raw/`（Git默认忽略），已随仓库提供的小规模资源放在 `data/`。下载记录和SHA-256写入 `data/download-log.json`。受限或未明确许可的数据不自动镜像到GitHub。

## 来源

- https://github.com/yecchen/MIRAI
- https://doi.org/10.1145/3774904.3792306

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
