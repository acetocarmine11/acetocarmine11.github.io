from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
import sys
import time
import traceback
from fake_useragent import UserAgent

def setup_scholarly():
    """配置scholarly库以处理潜在的网络问题"""
    print("🔧 配置scholarly库...")
    
    # 设置用户代理
    try:
        ua = UserAgent()
        user_agent = ua.random
        print(f"📱 使用用户代理: {user_agent}")
        
        # 配置scholarly的设置
        scholarly.set_timeout(30)  # 设置30秒超时
        print("⏰ 设置超时为30秒")
        
    except Exception as e:
        print(f"⚠️  用户代理设置失败: {e}")
        print("🔄 使用默认配置继续...")

def get_scholar_data():
    """获取Google Scholar数据"""
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
    if not scholar_id:
        raise ValueError("❌ GOOGLE_SCHOLAR_ID 环境变量未设置")
    
    print(f"🔍 开始搜索学者ID: {scholar_id}")
    
    try:
        # 搜索作者
        print("📡 正在连接Google Scholar...")
        author = scholarly.search_author_id(scholar_id)
        print(f"✅ 找到作者: {author.get('name', 'Unknown')}")
        
        # 填充详细信息
        print("📊 正在获取详细数据...")
        print("  - 基本信息...")
        scholarly.fill(author, sections=['basics'])
        print("  - 引用指标...")
        scholarly.fill(author, sections=['indices'])
        print("  - 引用计数...")
        scholarly.fill(author, sections=['counts'])
        print("  - 发表论文...")
        scholarly.fill(author, sections=['publications'])
        
        print(f"✅ 数据获取完成！")
        print(f"  📝 姓名: {author.get('name', 'N/A')}")
        print(f"  🏛️  机构: {author.get('affiliation', 'N/A')}")
        print(f"  📚 总引用数: {author.get('citedby', 0)}")
        print(f"  📈 h-index: {author.get('hindex', 0)}")
        print(f"  📊 i10-index: {author.get('i10index', 0)}")
        print(f"  📄 发表论文数: {len(author.get('publications', []))}")
        
        return author
        
    except Exception as e:
        print(f"❌ 获取学者数据时发生错误:")
        print(f"   错误类型: {type(e).__name__}")
        print(f"   错误信息: {str(e)}")
        print(f"   完整堆栈跟踪:")
        traceback.print_exc()
        raise

def save_data(author):
    """保存数据到文件"""
    print("💾 开始保存数据...")
    
    # 准备数据
    name = author['name']
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']:v for v in author['publications']}
    
    # 确保results目录存在
    os.makedirs('results', exist_ok=True)
    print("📁 results目录已准备")
    
    # 保存完整数据
    print("💾 保存完整学者数据...")
    with open(f'results/gs_data.json', 'w', encoding='utf-8') as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)
    print("✅ gs_data.json 已保存")
    
    # 保存Shield.io数据
    print("🛡️  保存Shield.io数据...")
    shieldio_data = {
      "schemaVersion": 1,
      "label": "citations",
      "message": f"{author['citedby']}",
    }
    with open(f'results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)
    print("✅ gs_data_shieldsio.json 已保存")
    
    # 保存日志
    print("📋 更新引用日志...")
    save_citation_log(author)
    print("✅ citation_log.json 已更新")

def save_citation_log(author):
    """保存引用历史日志"""
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
    
    # 读取现有日志
    if os.path.exists(log_file_path):
        try:
            with open(log_file_path, 'r', encoding='utf-8') as f:
                logs = json.load(f)
                print(f"📜 读取到 {len(logs)} 条历史记录")
        except Exception as e:
            print(f"⚠️  读取日志文件失败: {e}")
            logs = []
    else:
        logs = []
        print("📝 创建新的日志文件")
    
    # 添加新记录
    logs.append(log_entry)
    
    # 保存日志
    with open(log_file_path, 'w', encoding='utf-8') as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)
    
    print(f"📊 新日志条目: 引用数={log_entry['citations']}, h-index={log_entry['h_index']}")

def main():
    """主函数"""
    print("🚀 Google Scholar 爬虫开始运行")
    print(f"⏰ 运行时间: {datetime.now()}")
    print(f"🐍 Python版本: {sys.version}")
    print("=" * 50)
    
    try:
        # 配置scholarly
        setup_scholarly()
        print()
        
        # 获取数据
        author = get_scholar_data()
        print()
        
        # 保存数据
        save_data(author)
        print()
        
        print("🎉 所有操作完成！")
        print("=" * 50)
        
        # 输出摘要信息
        print("📋 运行摘要:")
        print(f"  ✅ 学者: {author['name']}")
        print(f"  ✅ 引用数: {author['citedby']}")
        print(f"  ✅ 数据文件已生成")
        print("🚀 程序正常结束")
        
    except KeyboardInterrupt:
        print("\n⚠️  程序被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 程序执行失败:")
        print(f"   错误: {str(e)}")
        print("\n🔍 详细错误信息:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 