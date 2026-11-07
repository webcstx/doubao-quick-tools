"""Quick AI 分词器"""

class Tokenizer:
    def __init__(self):
        self.vocab_size = 10000
    
    def encode(self, text):
        return [ord(c) for c in text[:200]]
    
    def decode(self, tokens):
        return ''.join(chr(t) for t in tokens if 32 <= t < 127)
    
    def count(self, text):
        return len(self.encode(text))

tokenizer = Tokenizer()
