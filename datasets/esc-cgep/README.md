# ESC-CGEP

> 当前下载状态：**partial**。已保存SeDGPL作者发布的ESCSubWoRe.npy及事件词典/映射。 已验证NumPy文件头，未执行对象反序列化；尚未确认其全部样本/候选与AECR论文采用版本完全一致。 详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


ESC因果图中的后继事件选择任务。

## 用途与版本

- 研究用途：检验抽象规则是否改善因果图预测。
- 固定版本：ESC-CGEP（AECR论文采用版本）
- 获取状态：`partial_download`
- 数据许可：未核实数据许可

保留官方候选集及划分；MAVEN 为512候选，ESC 为256候选，不使用本文件的两候选示例计算论文结果。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show esc-cgep
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch esc-cgep` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- **CGEP 数据集来源论文**：[What Would Happen Next? Predicting Consequences from An Event Causality Graph](https://aclanthology.org/2024.findings-emnlp.45/)（Chuanhong Zhan 等，Findings of EMNLP 2024）。
- **上游 ESC 语料论文**：[The Event StoryLine Corpus: A New Benchmark for Causal and Temporal Relation Extraction](https://aclanthology.org/W17-2711/)（Tommaso Caselli、Piek Vossen，Events and Stories in the News 2017）。
- **本项目采用的数据入口及后续使用论文**：[Abstract Event Causal Rules: Induction and Application](https://arxiv.org/abs/2608.05205)（Ziwei Zheng、Peiqiong Chen、Bang Wang，arXiv 预印本，2026）。
- **版本说明**：当前保存 SeDGPL 的 ESC 辅助结构及映射；它们不能直接视为 AECR 论文使用的完整 ESC-CGEP 版本。

- https://anonymous.4open.science/r/AECR-AFAF/
- https://arxiv.org/abs/2608.05205

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
