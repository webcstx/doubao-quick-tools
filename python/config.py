"""
Quick AI 配置文件
"""

# 模型配置
MODEL_CONFIG = {
    "name": "Quick AI",
    "version": "2.0.0",
    "hidden_dim": 512,
    "num_layers": 6,
    "num_heads": 8,
    "vocab_size": 10000,
    "max_seq_len": 512,
}

# 训练配置
TRAIN_CONFIG = {
    "batch_size": 32,
    "learning_rate": 3e-4,
    "epochs": 100,
    "warmup_steps": 1000,
}

# 推理配置
INFERENCE_CONFIG = {
    "max_new_tokens": 100,
    "temperature": 0.7,
    "top_p": 0.9,
    "do_sample": True,
}
