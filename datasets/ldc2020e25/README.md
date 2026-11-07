# LDC2020E25

LDC模式学习语料及论文派生复杂事件图。

## 用途与版本

- 研究用途：复杂图结构、补全及预测。
- 固定版本：LDC2020E25；派生8/12节点图另列版本
- 获取状态：`restricted_access`
- 数据许可：LDC 授权条款，未获取原始数据

先确认 LDC 访问资格和授权；派生样本数不是原始文档数。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show ldc2020e25
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

无已核实的自动下载资产；从下列作者入口获取并核对版本。

原始下载保存于 `raw/`（Git默认忽略），已随仓库提供的小规模资源放在 `data/`。下载记录和SHA-256写入 `data/download-log.json`。受限或未明确许可的数据不自动镜像到GitHub。

## 来源

- https://www.ldc.upenn.edu/
- https://github.com/snowfalling77/ReST-Pre

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
