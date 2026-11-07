# proScript

日常活动的部分有序脚本。

## 用途与版本

- 研究用途：简单时序结构和跨领域泛化。
- 固定版本：论文1使用的2,077场景子集需另行核对
- 获取状态：`downloadable_license_unverified`
- 数据许可：未核实数据许可

原始 proScript 全集与论文1评测子集规模不同；不提供层级关系评测。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show proscript
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

python scripts/datasets.py fetch proscript

作者提供 proscript_v1a.zip；完整原始集与论文1的评测子集须分开核对。

原始下载保存于 `raw/`（Git默认忽略），已随仓库提供的小规模资源放在 `data/`。下载记录和SHA-256写入 `data/download-log.json`。受限或未明确许可的数据不自动镜像到GitHub。

## 来源

- https://keisuke-sakaguchi.github.io/proscript/

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
