# ConceptNet

> 当前下载状态：**downloaded**。ConceptNet 5.7.0完整多语言断言CSV.gz（497,963,447字节，6片），不是英语抽样。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


概念级常识关系知识资源。

## 用途与版本

- 研究用途：本体先验与关系候选。
- 固定版本：ConceptNet 5；采用具体发布版本时需固定
- 获取状态：`bundled`
- 数据许可：数据通常为 CC-BY-SA-4.0，须以所下载发布说明为准

代码许可与数据许可不同；知识边不是特定新闻事件的真值。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show conceptnet
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch conceptnet` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://conceptnet.io/
- https://github.com/commonsense/conceptnet5

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
