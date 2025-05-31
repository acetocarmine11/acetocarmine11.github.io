# Citation日志功能说明

## 功能概述
此功能会在每次获取Google Scholar citation数据时自动记录日志，包括：
- 获取时间戳
- 引用数（citations）
- H指数（h_index）
- i10指数（i10_index）
- 作者姓名
- 所属机构
- 总发表数

## 日志文件位置
日志文件保存在：`google_scholar_crawler/results/citation_log.json`

## 日志格式
```json
[
  {
    "timestamp": "2024-01-01 08:00:00.000000",
    "citations": 10,
    "h_index": 2,
    "i10_index": 1,
    "name": "Author Name",
    "affiliations": "University Name",
    "total_publications": 5
  }
]
```

## 查看日志
使用提供的Python脚本查看日志：
```bash
cd google_scholar_crawler
python view_citation_log.py
```

或指定日志文件路径：
```bash
python view_citation_log.py path/to/citation_log.json
```

## 注意事项
- 日志文件会随着时间增长，建议定期备份
- 日志数据存储在`google-scholar-stats`分支中
- 每天8点UTC时间自动更新（通过GitHub Actions） 