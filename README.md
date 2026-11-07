# Quick AI 大模型

自研轻量级 AI 大模型，基于 Transformer 架构，支持智能对话和 AI 图像生成。

## 模型信息

- **名称**: Quick AI
- **版本**: v2.0.0
- **架构**: Transformer Decoder
- **参数量**: 6.3M
- **词表大小**: 10,000

## 功能

- 🤖 **智能对话**: 基于自研 Transformer 模型的聊天引擎
- 🎨 **图像生成**: 基于扩散模型 (Diffusion Model) 的 AI 生图
- ⚡ **轻量高效**: 纯 Python 实现，无需 GPU

## 快速开始

```bash
git clone https://github.com/webcstx/doubao-quick-tools.git
cd doubao-quick-tools

# 运行主程序
python3 python/main.py

# 单独运行聊天
python3 python/chat.py

# 单独运行生图
python3 python/image.py
```

## 项目结构

```
python/
├── main.py          # 主入口
├── model.py         # AI 模型核心 (Transformer)
├── tokenizer.py     # 分词器 (BPE)
├── config.py        # 模型/训练/推理配置
├── chat.py          # 聊天对话模块
├── image.py         # 图像生成模块 (Diffusion)
└── requirements.txt # 依赖列表
```

## 配置

在 `python/config.py` 中可以调整：
- 模型参数（隐藏层维度、层数、注意力头数）
- 训练参数（学习率、batch size、epoch）
- 推理参数（温度、top_p、最大生成长度）

## 许可证

Apache License 2.0
