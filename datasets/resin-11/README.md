# RESIN-11

11类新闻场景的时序及层级模式参考库。

## 用途与版本

- 研究用途：模式节点与时序、层级边归纳评测。
- 固定版本：文献中的 RESIN-11 评测版本
- 获取状态：`version_verification_required`
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

原始下载保存于 `raw/`（Git默认忽略），已随仓库提供的小规模资源放在 `data/`。下载记录和SHA-256写入 `data/download-log.json`。受限或未明确许可的数据不自动镜像到GitHub。

## 来源

- https://github.com/limanling/temporal-graph-schema
- https://github.com/raspberryice/inc-schema

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
