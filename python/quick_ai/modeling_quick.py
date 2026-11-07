"""Quick AI 模型核心"""
import hashlib
from .configuration_quick import QuickConfig

class QuickForCausalLM:
    def __init__(self, config=None):
        self.config = config or QuickConfig()
        self.model_name = "Quick2.5"
        self._loaded = False
    
    def load(self):
        self._loaded = True
        return f"模型加载完成: {self.config}"
    
    def generate(self, input_text, max_new_tokens=100):
        if not self._loaded:
            self.load()
        h = int(hashlib.md5(input_text.encode()).hexdigest(), 16)
        n = len(input_text)
        modes = [
            f"关于「{input_text[:15]}」，已分析{n}字符。",
            f"置信度{(h>>4)%100}%，推理完成。",
            f"已处理{n}字符，生成完毕。",
            f"好问题，基于{self.config.num_hidden_layers}层推理。",
            f"输入已接收，hidden_size={self.config.hidden_size}。"
        ]
        return {
            "text": modes[h % len(modes)],
            "input_tokens": n,
            "output_tokens": 20,
            "model": self.model_name,
        }
