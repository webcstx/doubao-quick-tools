"""Quick AI 模型配置"""
from dataclasses import dataclass

@dataclass
class QuickConfig:
    hidden_size: int = 512
    num_hidden_layers: int = 6
    num_attention_heads: int = 8
    max_position_embeddings: int = 2048
    vocab_size: int = 151936
    
    @classmethod
    def from_size(cls, size="0.5B"):
        presets = {
            "0.5B": {"hidden_size": 512, "num_hidden_layers": 6, "num_attention_heads": 8},
            "1.5B": {"hidden_size": 1536, "num_hidden_layers": 28, "num_attention_heads": 12},
            "3B": {"hidden_size": 2048, "num_hidden_layers": 36, "num_attention_heads": 16},
        }
        return cls(**presets[size])
    
    def __repr__(self):
        return f"QuickConfig(hidden={self.hidden_size}, layers={self.num_hidden_layers})"
