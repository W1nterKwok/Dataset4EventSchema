# HiEve（文本事件层级）

> 当前下载状态：**downloaded**。公开清洗版hievents_v2全部文件，含100篇processed文档与上游提供的特征文件；原始RAR地址404。  详细文件状态见 [DOWNLOAD_STATUS.md](DOWNLOAD_STATUS.md)。


新闻中的事件层级及子事件关系语料。

## 用途与版本

- 研究用途：层级关系抽取。
- 固定版本：公开清洗版HiEve_Dataset的固定提交，100篇processed文档；包含传递闭包
- 获取状态：`bundled`
- 数据许可：未核实数据许可

注意区分同名的 Human-in-Events 视频数据集；论文地址及下载地址均应在正式使用前核实。

## 示例与注释

[`example.json`](example.json) 包含 `record` 及独立的中文字段注释 `_说明`。示例类型为 `illustrative_template`。仅 `upstream_record` 是作者公开记录；`illustrative_template` 是本项目自编格式演示，不能冒充真实数据。

```bash
python scripts/datasets.py show hieve
```

从仓库根目录执行。`_说明` 是本项目的包装字段，不属于原始数据格式。真实样本与标注不得直接用于待预测输入。

## 获取数据

文件已保存于本目录data。可运行 `python scripts/datasets.py fetch hieve` 校验已存文件；分片归档用restore命令合并。

本次已取得的公开原始数据保存于 `data/` 并提交Git；大归档按清单分片，合并输出至 `raw/`。下载记录和SHA-256写入 `data/download-log.json`。归档范围和原始权利说明见下载状态与许可记录。

## 来源

- https://aclanthology.org/L14-1020/

核对日期：2026-11-07。完整机器可读信息见 [`metadata.json`](metadata.json)。
