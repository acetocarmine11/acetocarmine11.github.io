# Google Scholar Citation Crawler

这个工具用于自动获取Google Scholar上的引用数据，具有详细的调试信息和错误处理功能。

## 功能

- 获取作者的基本信息（姓名、机构等）
- 获取引用统计（总引用数、h-index、i10-index）
- 获取发表论文列表
- 生成Shield.io格式的徽章数据
- 记录历史引用数据日志
- 详细的调试信息和错误处理
- 网络连接诊断和测试

## 使用方法

### 本地运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 设置环境变量：
```bash
export GOOGLE_SCHOLAR_ID="your_google_scholar_id"
```

3. 运行脚本：
```bash
python main.py
```

### 网络和环境测试

在运行主脚本之前，建议先运行测试脚本检查环境：

```bash
python test_network.py
```

这个测试脚本会检查：
- 必要的Python库是否正确安装
- 网络连接是否正常
- 环境变量是否设置
- scholarly库基本功能是否可用

### GitHub Action自动运行

该项目配置了GitHub Action，具有以下特性：
- 每天早上8点自动运行
- 可以手动触发
- 详细的调试和诊断信息
- 网络连接测试
- 超时保护（30分钟总时长，爬虫20分钟）
- 失败时自动上传日志文件
- 将结果推送到`google-scholar-stats`分支

## 输出文件

运行后会在`results/`目录生成以下文件：
- `gs_data.json` - 完整的学者数据
- `gs_data_shieldsio.json` - Shield.io徽章数据
- `citation_log.json` - 历史引用数据日志

## 环境变量

- `GOOGLE_SCHOLAR_ID` - 您的Google Scholar ID（必需）

## 故障排除

### 常见问题

1. **网络连接问题**
   - 运行 `python test_network.py` 检查网络状态
   - 确保可以访问 `scholar.google.com`
   - GitHub Action服务器可能受到Google的反爬虫限制

2. **依赖安装问题**
   - 确保Python版本≥3.7
   - 使用 `pip install -r requirements.txt --verbose` 查看详细安装信息

3. **Google Scholar ID错误**
   - 确保ID格式正确（通常是字符串）
   - 确保对应的Google Scholar个人资料是公开的

4. **超时问题**
   - 脚本设置了30秒的网络超时
   - GitHub Action设置了20分钟的运行超时
   - 如果经常超时，可能是网络限制问题

### 调试信息

主脚本 `main.py` 现在包含详细的调试信息：
- 🚀 启动信息和系统状态
- 📡 网络连接状态
- 📊 数据获取进度
- 💾 文件保存状态
- ❌ 详细的错误信息和堆栈跟踪

GitHub Action workflow 包含：
- 🖥️ 系统信息
- 🌐 网络诊断
- 📦 依赖安装验证
- 🔍 库导入测试
- 📊 运行日志和文件检查

### 查看GitHub Action日志

1. 进入GitHub仓库
2. 点击 "Actions" 标签
3. 选择最近的 "Get Citation Data" 运行
4. 查看详细的步骤日志
5. 如果失败，可以下载 `crawler-logs` artifacts

## 注意事项

- 请确保您的Google Scholar个人资料是公开的
- 由于Google Scholar的反爬虫机制，建议不要过于频繁地运行
- GitHub Action已配置为每天运行一次，这个频率是合适的
- 如果在GitHub Action中遇到持续的网络问题，可能是服务器IP被限制，这是正常现象
- 可以尝试手动触发workflow，有时候网络状况会有所不同

## 技术细节

- 使用 `scholarly` 库访问Google Scholar
- 支持随机用户代理以避免检测
- 包含网络超时和重试机制
- 详细的日志记录和错误处理
- 支持UTF-8编码的中文输出 