# 当前核验记录

本次逐项下载核验已更新，完整结果以[原始数据下载与缺口](DOWNLOADS.md)、各数据集DOWNLOAD_STATUS.md、metadata.json及根目录download-status.json为准。

已取得文件均记录来源、大小和SHA-256；GitHub来源固定提交，RESPONSE和ECCKG额外核对官方MD5。原始文件保持字节不变；跨平台Git属性避免换行转换破坏校验。大归档分片后可合并并通过整体SHA-256核验。

目录一致性、样例来源标识、分类数据计数、问答配对、图引用及所有随附文件哈希由`python scripts/datasets.py validate`自动检查。二进制pickle和NumPy对象未自动反序列化。
