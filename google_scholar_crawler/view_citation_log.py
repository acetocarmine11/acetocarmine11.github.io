import json
import sys
from datetime import datetime

def view_citation_log(log_file='results/citation_log.json'):
    """查看和分析citation日志"""
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            logs = json.load(f)
        
        if not logs:
            print("日志文件为空")
            return
        
        print(f"总共有 {len(logs)} 条日志记录\n")
        
        # 显示最新的5条记录
        print("最近5条记录：")
        print("-" * 80)
        for log in logs[-5:]:
            print(f"时间: {log['timestamp']}")
            print(f"引用数: {log['citations']}")
            print(f"H指数: {log['h_index']}")
            print(f"i10指数: {log['i10_index']}")
            print(f"总发表数: {log['total_publications']}")
            print("-" * 80)
        
        # 计算引用数增长
        if len(logs) > 1:
            first_citation = logs[0]['citations']
            last_citation = logs[-1]['citations']
            growth = last_citation - first_citation
            print(f"\n引用数增长统计：")
            print(f"首次记录: {first_citation} (时间: {logs[0]['timestamp']})")
            print(f"最新记录: {last_citation} (时间: {logs[-1]['timestamp']})")
            print(f"总增长: {growth}")
            
    except FileNotFoundError:
        print(f"日志文件 {log_file} 不存在")
    except json.JSONDecodeError:
        print(f"日志文件 {log_file} 格式错误")
    except Exception as e:
        print(f"读取日志文件时出错: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        view_citation_log(sys.argv[1])
    else:
        view_citation_log() 