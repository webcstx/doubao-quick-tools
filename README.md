# Quick AI SDK

自研轻量级大模型 SDK，支持对话、图像生成、向量嵌入等能力。

## 安装

```bash
cd python/
pip install -e .
```

## 快速开始

```python
from quick_ai import QuickAIClient

# 初始化客户端
client = QuickAIClient()

# 对话
resp = client.chat.create("你好")
print(resp.text)

# 生图
resp = client.image.generate("一只猫")
print(resp.style)

# 向量
resp = client.embedding.embed("测试文本")
print(resp.dim)
```

## 项目结构

```
python/
├── quick_ai/           # SDK 核心包
│   ├── __init__.py     # 包入口
│   ├── client.py       # QuickAIClient 主客户端
│   ├── chat.py         # 对话模型
│   ├── image.py        # 图像生成模型
│   ├── embedding.py    # 向量嵌入模型
│   ├── config.py       # 配置
│   ├── errors.py       # 错误定义
│   └── utils.py        # 工具函数
├── examples/           # 示例代码
│   ├── chat_demo.py
│   └── image_demo.py
├── setup.py            # 安装脚本
└── requirements.txt    # 依赖
```

## API 文档

### QuickAIClient
- `client.chat.create(message)` - 创建对话
- `client.image.generate(prompt)` - 生成图像
- `client.embedding.embed(text)` - 生成向量
- `client.list_models()` - 列出支持的模型

## 许可证

Apache License 2.0
