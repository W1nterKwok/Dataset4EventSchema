# EECKG

> 当前下载状态：**downloaded**。ECCKG作者Zenodo v1全部五个文件；逐文件MD5与Zenodo官方记录一致。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


EV²构建所用事件演化常识知识资源。

## 用途与版本

- 研究用途：事件类型与关系的先验知识。
- 固定版本：作者Zenodo记录6084081，保留全部发布文件及官方MD5
- 获取状态：`bundled`
- 数据许可：CC-BY-4.0（作者Zenodo元数据）

EV²是评测基准，不等于EECKG全量知识图谱；不把两者作为同一数据集。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show eeckg
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch eeckg` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://arxiv.org/abs/2404.17513

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
