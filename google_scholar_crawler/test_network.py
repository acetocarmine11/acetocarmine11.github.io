#!/usr/bin/env python3
"""
Google Scholar 网络连接和依赖测试脚本
用于诊断网络问题和验证环境配置
"""

import sys
import time
import requests
from datetime import datetime

def test_imports():
    """测试必要的库导入"""
    print("🔍 测试Python库导入...")
    
    try:
        import scholarly
        print("  ✅ scholarly 导入成功")
    except ImportError as e:
        print(f"  ❌ scholarly 导入失败: {e}")
        return False
    
    try:
        import jsonpickle
        print("  ✅ jsonpickle 导入成功")
    except ImportError as e:
        print(f"  ❌ jsonpickle 导入失败: {e}")
        return False
    
    try:
        import fake_useragent
        print("  ✅ fake_useragent 导入成功")
    except ImportError as e:
        print(f"  ❌ fake_useragent 导入失败: {e}")
        return False
    
    return True

def test_network():
    """测试网络连接"""
    print("\n🌐 测试网络连接...")
    
    # 测试基本网络连接
    test_urls = [
        ("Google DNS", "https://8.8.8.8"),
        ("Google", "https://www.google.com"),
        ("Google Scholar", "https://scholar.google.com"),
    ]
    
    for name, url in test_urls:
        try:
            print(f"  🔗 测试 {name} ({url})...")
            response = requests.get(url, timeout=10, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            print(f"    ✅ 状态码: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"    ❌ 连接失败: {e}")
            return False
    
    return True

def test_scholarly_basic():
    """测试scholarly库基本功能"""
    print("\n📚 测试scholarly库基本功能...")
    
    try:
        from scholarly import scholarly
        
        # 设置超时
        scholarly.set_timeout(30)
        print("  ✅ 超时设置成功")
        
        # 测试搜索功能
        print("  🔍 测试搜索功能...")
        search_query = scholarly.search_author('Albert Einstein')
        first_author = next(search_query)
        print(f"    ✅ 找到作者: {first_author.get('name', 'Unknown')}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ scholarly测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_environment():
    """测试环境变量"""
    print("\n🔧 测试环境变量...")
    
    import os
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
    if scholar_id:
        print(f"  ✅ GOOGLE_SCHOLAR_ID 已设置: {scholar_id}")
        return True
    else:
        print("  ⚠️  GOOGLE_SCHOLAR_ID 未设置")
        print("    提示: 请设置环境变量 GOOGLE_SCHOLAR_ID")
        return False

def main():
    """主测试函数"""
    print("🚀 Google Scholar 环境测试开始")
    print(f"⏰ 测试时间: {datetime.now()}")
    print(f"🐍 Python版本: {sys.version}")
    print("=" * 60)
    
    tests = [
        ("库导入测试", test_imports),
        ("网络连接测试", test_network),
        ("环境变量测试", test_environment),
        ("scholarly基本功能测试", test_scholarly_basic),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        try:
            result = test_func()
            results.append((test_name, result))
            status = "✅ 通过" if result else "❌ 失败"
            print(f"  📊 结果: {status}")
        except Exception as e:
            print(f"  ❌ 测试异常: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("📋 测试总结:")
    
    all_passed = True
    for test_name, result in results:
        status = "✅" if result else "❌"
        print(f"  {status} {test_name}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n🎉 所有测试通过！环境配置正常。")
        print("💡 如果GitHub Action仍然失败，可能是服务器网络限制问题。")
    else:
        print("\n⚠️  有测试失败，请检查上述问题。")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 