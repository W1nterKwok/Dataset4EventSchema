# RESPONSE

灾害场景下结合资源缺失、时间窗口和解释的常识问答。

## 用途与版本

- 研究用途：危机场景中的时限推理与解释评测。
- 固定版本：数据 DOI v1；论文正式发表于 ECAI 2025，967–974页，DOI `10.3233/FAIA250904`，已通过作者机构 UCL 的存档核实。
- 获取状态：`download_blocked_403`
- 数据许可：CC-BY-NC-SA-4.0（DataCite DOI元数据已核实）

官方数据站及文件下载在本环境返回403；以下为项目自编接口演示，非官方原始样本。回答仅用于研究评测，不是现实应急指引。

论文摘要报告1,789条标注实例、6,037组问题；这些是论文报告的规模，尚未用下载文件重新统计。任务包含问题描述、缺失资源、立即/一周后/一月后的回答及解释。自动文本相似性指标应结合按时间范围的人类评价使用。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show response
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

无已核实的自动下载资产；从下列作者入口获取并核对版本。

原始下载保存于 `raw/`（Git默认忽略），已随仓库提供的小规模资源放在 `data/`。下载记录和SHA-256写入 `data/download-log.json`。受限或未明确许可的数据不自动镜像到GitHub。

## 来源

- https://doi.org/10.5522/04/26010064.v1
- https://arxiv.org/abs/2503.11348
- https://discovery.ucl.ac.uk/id/eprint/10213506/
- https://doi.org/10.3233/FAIA250904

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
