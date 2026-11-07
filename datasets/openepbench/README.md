# OpenEPBench

> 当前下载状态：**downloaded**。作者已公开且此前随仓库保存的数据文件。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


中英文自由文本未来事件预测。

## 用途与版本

- 研究用途：开放式和中文预测验证。
- 固定版本：作者公开 data/data/cn_valid_data.json 与 en_valid_data.json
- 获取状态：`bundled`
- 数据许可：MIT（作者仓库许可；新闻原文的权利仍归原权利人）

以每个问题形成时间作为截点；新闻截断不能清除模型参数记忆。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `upstream_record`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show openepbench
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

python scripts/datasets.py fetch openepbench

原始下载保存于 `raw/`（Git默认忽略），已随仓库提供的小规模资源放在 `data/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://github.com/ncepu-eai/OpenEP

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
