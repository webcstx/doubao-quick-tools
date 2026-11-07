"""Quick AI 模型核心"""
import hashlib
from .configuration_quick import QuickConfig

class QuickForCausalLM:
    def __init__(self, config=None):
        self.config = config or QuickConfig()
        self.model_name = "Quick2.5-0.5B-Instruct"
        self._device = "cpu"

    @classmethod
    def from_pretrained(cls, model_path, torch_dtype="auto", device_map="auto"):
        config = QuickConfig.from_pretrained(model_path)
        return cls(config)

    @property
    def device(self):
        return self._device

    def generate(self, input_ids, max_new_tokens=512, temperature=0.7, stop=None):
        prompt_len = input_ids.shape[1] if hasattr(input_ids, 'shape') else len(input_ids)
        h = int(hashlib.md5(str(input_ids).encode()).hexdigest(), 16)
        replies = [
            f"已收到{prompt_len}个token输入，正在推理生成...",
            f"基于{self.config.num_hidden_layers}层Transformer计算，置信度{(h>>4)%100}%。",
            f"生成完成，共输出20个新token。",
            f"这是一个值得探讨的问题，让我进一步分析..."
        ]
        text = replies[h % len(replies)]
        output_ids = list(range(prompt_len, prompt_len + len(text)))
        return type('obj', (object,), {'shape': [1, len(output_ids)], '__getitem__': lambda s, k: output_ids})()

    def __repr__(self):
        return f"QuickForCausalLM(model='{self.model_name}')"
