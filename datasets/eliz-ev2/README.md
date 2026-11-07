# Eliz-EV²

ElizBench的事件泛化子集：根据具体事件描述，选择其对应的抽象事件类别。SSR-EG是作者提出的方法，本目录整理的是数据，未运行模型推理。

## 已随附的作者数据

| 文件 | 内容 | 实测规模 |
| --- | --- | --- |
| [`Eliz-EV2.csv`](data/Eliz-EV2.csv) | 逐样本输入与金标 | 1,331条、46类 |
| [`Eliz-EV2_info.csv`](data/Eliz-EV2_info.csv) | 类别候选和统计 | 46行 |

两个文件均从固定提交 `fab7749d89a44328624e4477f8cb2cf0b81ca7c6` 取得，保留原始字节及SHA-256。类别计数逐类与成品数据核对一致；上游MIT许可证见 [`LICENSE.upstream`](LICENSE.upstream)。上游EV²/MAVEN及新闻原文的权利仍须遵守。

## 字段和示例

[`example.json`](example.json) 是首条真实记录，附中文字段注释。原始CSV字段为 `specific_event, abstract_event`，类别统计表字段为 `abstract_event, specific_event_count`。

公开文件1,331条，比论文所述1,383条少52条。本仓库固定该公开版本，不补造缺失样本。既有实验归档中还存在不同样本规模，比较模型时应使用同一版本和样本集合。

```bash
python datasets/eliz-ev2/example.py
python scripts/datasets.py show eliz-ev2
python scripts/datasets.py inspect eliz-ev2
python scripts/datasets.py fetch eliz-ev2
python scripts/datasets.py validate
```

从仓库根目录执行；示例代码仅使用Python标准库，输出模型输入和独立的评测金标，不调用任何模型API。`fetch`可校验或恢复原始文件。

## 研究使用边界

公开文件为1,331条/46类；与论文描述的1,383条不同，不得混作同一版本；这是事件类别泛化，不是原始EV²的CEC/CRR任务。

公开CSV不包含正式的train/dev/test列。候选类别可由info表读取；如自行训练或调参，应另行设计并记录划分，不能宣称是作者官方划分。评测可使用按样本支持数加权的Precision、Recall、F1，并保留每类指标；不能把此分类结果直接解释为完整事件模式图归纳质量。

方法复现、公开版本差异和相关资源见[ElizBench整理说明](../../docs/ELIZBENCH.md)。本目录未镜像作者的模型输出归档、源数据全集或API配置。

## 来源

- [作者仓库](https://github.com/michiru-39/ElizBench_SSR-EG)
- [固定版本数据目录](https://github.com/michiru-39/ElizBench_SSR-EG/tree/fab7749d89a44328624e4477f8cb2cf0b81ca7c6/ElizBench-dataset)
- [论文 DOI](https://doi.org/10.1016/j.ipm.2026.104851)

核验日期：2026-11-07。
