"""Quick AI 配置"""
MODEL = {"hidden_dim": 512, "num_layers": 6, "num_heads": 8, "vocab_size": 10000}
TRAIN = {"batch_size": 32, "lr": 3e-4, "epochs": 100}
INFER = {"temperature": 0.7, "top_p": 0.9, "max_tokens": 100}
