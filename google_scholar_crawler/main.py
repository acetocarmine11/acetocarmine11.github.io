from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

# 添加日志记录功能
log_file_path = 'results/citation_log.json'
log_entry = {
    'timestamp': str(datetime.now()),
    'citations': author['citedby'],
    'h_index': author['hindex'],
    'i10_index': author['i10index'],
    'name': author['name'],
    'affiliations': author.get('affiliation', 'N/A'),
    'total_publications': len(author['publications'])
}

# 读取现有日志（如果存在）
if os.path.exists(log_file_path):
    with open(log_file_path, 'r', encoding='utf-8') as f:
        logs = json.load(f)
else:
    logs = []

# 添加新的日志条目
logs.append(log_entry)

# 保存更新后的日志
with open(log_file_path, 'w', encoding='utf-8') as f:
    json.dump(logs, f, ensure_ascii=False, indent=2)

print(f"Log entry added: {log_entry}")
