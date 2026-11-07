# ElizBench / SSR-EG 数据整理

本次新增两个独立目录：[Eliz-EV²](../datasets/eliz-ev2/)和[Eliz-MAVEN](../datasets/eliz-maven/)。两者属于同一ElizBench基准；SSR-EG是事件泛化方法，不另计为数据集。

| 子集 | 实际公开样本数 | 抽象类别数 | 原始字段 |
| --- | --- | --- | --- |
| Eliz-EV² | 1,331 | 46 | specific_event、abstract_event |
| Eliz-MAVEN | 4,374 | 39 | specific_event、abstract_event、trigger、trigger_offset |

总计5,705条。统计由CSV解析后重新计算，两份info表的类别和逐类样本计数均与成品CSV一致；Eliz-MAVEN每类不同触发词数也已核对。四个CSV随本仓库提供，均固定于作者提交 `fab7749d89a44328624e4477f8cb2cf0b81ca7c6`，元数据记录SHA-256。

## 版本和来源

作者README仍写旧目录`Eliz-dataset/`，当前实际目录是`ElizBench-dataset/`。数据应按固定提交的真实文件获取。

Eliz-EV²公开成品为1,331条，论文描述为1,383条，相差52条；本次没有补造样本。模型比较应固定同一公开成品输入，不能把不同归档规模的结果当成统一测试集。Eliz-MAVEN为从MAVEN派生的事件泛化数据，与MAVEN-ERE、MAVEN-CGEP和MAVEN-AECR分别管理。

原始文件没有稳定样本ID或正式train/dev/test列。若需要内部索引，应注明是本项目添加的CSV数据行序号，并保持源文件哈希；按需设计划分及去重策略，避免同源句子进入训练和测试。

## 输入、金标与指标

两个`example.py`直接读取真实CSV。模型输入为specific_event和完整候选类别；abstract_event仅供评测。Eliz-MAVEN的trigger和trigger_offset也默认只用于分析，若实验向模型提供真值触发词，应单列实验条件。

trigger_offset是CSV字符串中的JSON数组，表示原始MAVEN句子的token跨度，0起始、左闭右开；不是字符跨度。展示句子的空格分词不保证与原始tokens一致。

建议报告按真实类别样本支持数加权的Precision、Recall、F1，以及每类结果和样本数。分类指标衡量事件类别泛化，不能替代模式节点、时序边、层级边的图结构评测。本次没有调用真实模型API，也没有重新运行SSR-EG实验。

## 许可与引用

作者仓库为MIT，每个子集保留完整`LICENSE.upstream`。原始EV²/MAVEN及新闻文本的权利不会因本次整理重新授权。

- [作者仓库](https://github.com/michiru-39/ElizBench_SSR-EG)
- [固定版本数据](https://github.com/michiru-39/ElizBench_SSR-EG/tree/fab7749d89a44328624e4477f8cb2cf0b81ca7c6/ElizBench-dataset)
- [论文：Benchmarking and enhancing the ability of large language models on event generalization](https://doi.org/10.1016/j.ipm.2026.104851)

核验日期：2026-11-07。
