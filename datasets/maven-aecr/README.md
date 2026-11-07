# MAVEN-AECR

> 当前下载状态：**downloaded**。作者公开733条抽象规则、规则映射、聚类输出及检索训练配对文件；保留作者命名。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


具体因果事件对和抽象因果规则的配对资源。

## 用途与版本

- 研究用途：规则归纳、质量评估与规则检索。
- 固定版本：MAVEN-AECR（分别733/180条规则，文献报告）
- 获取状态：`bundled`
- 数据许可：未核实数据许可

规则库构建文档和下游测试文档的重叠需核查；规则检索划分不等于 CGEP 划分。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show maven-aecr
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch maven-aecr` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://anonymous.4open.science/r/AECR-AFAF/
- https://arxiv.org/abs/2608.05205

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
