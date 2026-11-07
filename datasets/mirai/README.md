# MIRAI（论文10设置）

> 当前下载状态：**partial**。已保存完整MIRAI官方发布包（581,967,516字节，7片），另提取705条测试查询和100条子集查询。 原始包实测296,630条新闻、589,930条历史KG记录；不直接声称等同于论文10所列152,500历史事件的筛选版本。 详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


结构化历史事件与新闻文本结合的关系集合预测。

## 用途与版本

- 研究用途：新闻证据驱动的事件预测。
- 固定版本：Thinking Bidirectionally 使用的查询/筛选版本
- 获取状态：`partial_download`
- 数据许可：未核实数据许可

MIRAI 原始仓库是资源起点；未核实其与论文10所用705查询版本完全一致，不将原版统计直接套用到论文10。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show mirai
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch mirai` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://github.com/yecchen/MIRAI
- https://doi.org/10.1145/3774904.3792306

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
