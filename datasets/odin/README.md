# ODIN

> 当前下载状态：**downloaded**。作者已公开且此前随仓库保存的数据文件。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


18类开放域场景的人工修订事件模式。

## 用途与版本

- 研究用途：开放场景及跨场景模式归纳。
- 固定版本：odin_curated @ 2dd968b94ae5cdd2a3d1e3c1decbf5b416cc2248
- 获取状态：`bundled`
- 数据许可：GPL-3.0（上游仓库许可；保留完整许可证）

作者方法生成后人工修订；与 RESIN-11 交叉验证。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `upstream_record`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show odin
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

python scripts/datasets.py fetch odin

原始下载保存于 `raw/`（Git默认忽略），已随仓库提供的小规模资源放在 `data/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://github.com/raspberryice/inc-schema

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
