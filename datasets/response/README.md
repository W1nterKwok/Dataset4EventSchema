# RESPONSE

> 当前下载状态：**downloaded**。DOI v1官方发布的all_questions_v1.json、all_questions_v2.json及官方元数据；由GitHub下载任务取得并通过官方MD5。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


灾害场景下结合资源缺失、时间窗口和解释的常识问答。

## 用途与版本

- 研究用途：危机场景中的时限推理与解释评测。
- 固定版本：数据 DOI v1；论文 ECAI 2025，DOI 10.3233/FAIA250904
- 获取状态：`bundled`
- 数据许可：CC-BY-NC-SA-4.0（DataCite DOI元数据已核实）

此前本机返回403；本次通过仓库官方下载任务取得两个原始JSON，示例现为第一条真实记录。回答仅用于研究评测，不是现实应急指引。

论文摘要报告1,789条标注实例、6,037组问题；这是论文报告的规模；本次取得的两个官方发布文件分别有962和949条记录，不直接等同于论文筛选后的统计。任务包含问题描述、缺失资源、立即/一周后/一月后的回答及解释。自动文本相似性指标应结合按时间范围的人类评价使用。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `upstream_record`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show response
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch response` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- **来源论文**：[RESPONSE: Benchmarking the Ability of Language Models to Undertake Commonsense Reasoning in Crisis Situation](https://doi.org/10.3233/FAIA250904)（Aissatou Diallo 等，ECAI 2025）。

- https://doi.org/10.5522/04/26010064.v1
- https://arxiv.org/abs/2503.11348
- https://discovery.ucl.ac.uk/id/eprint/10213506/
- https://doi.org/10.3233/FAIA250904

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
