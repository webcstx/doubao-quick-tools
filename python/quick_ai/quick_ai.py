"""Quick AI 高级接口"""
from .configuration_quick import QuickConfig
from .modeling_quick import QuickForCausalLM
from .tokenization_quick import QuickTokenizer

class QuickAI:
    def __init__(self, size="0.5B"):
        self.config = QuickConfig.from_size(size)
        self.model = QuickForCausalLM(self.config)
        self.tokenizer = QuickTokenizer()
        self.size = size
        self.model_name = f"Quick2.5-{size}"
    
    def chat(self, message):
        result = self.model.generate(message)
        return result["text"]
    
    def generate(self, prompt, **kwargs):
        return self.model.generate(prompt, **kwargs)
    
    def info(self):
        params = self.config.hidden_size ** 2 * self.config.num_hidden_layers * 4
        return {
            "model": self.model_name,
            "size": self.size,
            "params": f"{params/1e9:.2f}B",
            "layers": self.config.num_hidden_layers,
        }
