"""Quick AI 模型配置"""
from dataclasses import dataclass

@dataclass
class QuickConfig:
    hidden_size: int = 512
    intermediate_size: int = 1376
    num_hidden_layers: int = 6
    num_attention_heads: int = 8
    num_key_value_heads: int = 2
    max_position_embeddings: int = 2048
    vocab_size: int = 151936
    rms_norm_eps: float = 1e-6
    rope_theta: float = 10000.0

    @classmethod
    def from_pretrained(cls, model_path):
        return cls()

    def __repr__(self):
        return f"QuickConfig(hidden={self.hidden_size}, layers={self.num_hidden_layers})"
