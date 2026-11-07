# Quick AI 2.5

自研轻量级大模型，参考 Qwen2.5 架构设计。

## 模型尺寸

| 尺寸 | 隐藏层 | 层数 | 参数量 |
|------|--------|------|--------|
| 0.5B | 512 | 6 | 6.3M |
| 1.5B | 1536 | 28 | 264M |
| 3B | 2048 | 36 | 604M |

## 快速开始

```python
from quick_ai import QuickAI

# 初始化模型
ai = QuickAI(size="0.5B")

# 对话
print(ai.chat("你好"))

# 生成
print(ai.generate("写一首诗"))
```

## 项目结构

```
python/
├── quick_ai/
│   ├── __init__.py
│   ├── configuration_quick.py    # 模型配置
│   ├── modeling_quick.py         # 模型核心
│   ├── tokenization_quick.py     # 分词器
│   └── quick_ai.py               # 高级接口
├── examples/
│   ├── chat/                     # 对话示例
│   ├── generation/               # 生成示例
│   └── function_calling/         # 函数调用示例
├── setup.py
└── requirements.txt
```

## 许可证

Apache License 2.0
