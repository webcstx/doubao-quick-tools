"""Quick AI 分词器"""

class QuickTokenizer:
    SPECIAL_TOKENS = {
        "<|im_start|>": 151644,
        "<|im_end|>": 151645,
        "<|endoftext|>": 151643,
    }

    def __init__(self):
        self.vocab_size = 151936

    @classmethod
    def from_pretrained(cls, model_path):
        return cls()

    def encode(self, text, add_special_tokens=True):
        tokens = []
        if add_special_tokens:
            tokens.append(self.SPECIAL_TOKENS["<|im_start|>"])
        for c in text:
            tokens.append(ord(c) if 32 <= ord(c) < 127 else 1000)
        if add_special_tokens:
            tokens.append(self.SPECIAL_TOKENS["<|im_end|>"])
        return tokens

    def decode(self, tokens):
        return ''.join(chr(t) for t in tokens if 32 <= t < 127)

    def apply_chat_template(self, messages):
        out = ""
        for m in messages:
            out += f"<|im_start|>{m['role']}\n{m['content']}<|im_end|>\n"
        out += "<|im_start|>assistant\n"
        return out
