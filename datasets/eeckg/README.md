# EECKG

EV²构建所用事件演化常识知识资源。

## 用途与版本

- 研究用途：事件类型与关系的先验知识。
- 固定版本：EV²所引 EECKG；独立原始资源地址待核实
- 获取状态：`source_verification_required`
- 数据许可：未核实数据许可

EV²是评测基准，不等于EECKG全量知识图谱；不把两者作为同一数据集。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show eeckg
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

无已核实的自动下载资产；从下列作者入口获取并核对版本。

原始下载保存于 `raw/`（Git默认忽略），已随仓库提供的小规模资源放在 `data/`。下载记录和SHA-256写入 `data/download-log.json`。受限或未明确许可的数据不自动镜像到GitHub。

## 来源

- https://arxiv.org/abs/2404.17513

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
