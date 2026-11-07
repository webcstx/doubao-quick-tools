# Quick AI 2.5

自研轻量级大模型，参考 Qwen2.5-0.5B-Instruct 推理流程设计。

## 推理流程

严格遵循 Qwen2.5 的 6 步推理：
1. 加载分词器（Tokenizer）
2. 加载模型配置 + 权重
3. 构造指令模板（`<|im_start|>` 格式）
4. 文本转 Tensor
5. `model.generate()` 循环预测下一个 token
6. 解码输出文本

## 快速开始

```bash
cd python/
pip install -r requirements.txt
python examples/chat.py
```

## 项目结构

```
python/
├── quick_ai/
│   ├── __init__.py
│   ├── configuration_quick.py    # 模型配置（参考 Qwen2Config）
│   ├── modeling_quick.py         # 模型核心（参考 Qwen2ForCausalLM）
│   └── tokenization_quick.py     # 分词器（参考 Qwen2Tokenizer）
├── examples/
│   └── chat.py                   # 推理入口脚本
├── requirements.txt              # 依赖：torch, transformers, accelerate...
└── setup.py
```

## 依赖

```txt
torch>=2.0.0
transformers>=4.37.0
accelerate>=0.26.0
tokenizers>=0.15.0
sentencepiece>=0.1.99
```

## 说明

- 代码仓库 = 运行逻辑 + 示例脚本
- 模型权重（.safetensors）= 训练好的参数，需单独下载
- 两者配合才能真正运行 AI 推理

## 许可证

Apache License 2.0
