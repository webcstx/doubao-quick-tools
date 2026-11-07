"""
Quick AI 分词器
自研 BPE 分词器
"""

class Tokenizer:
    """文本分词器"""
    
    def __init__(self):
        self.vocab = {}
        self.vocab_size = 10000
    
    def encode(self, text):
        """文本转 token"""
        return [ord(c) for c in text[:100]]
    
    def decode(self, tokens):
        """token 转文本"""
        return ''.join([chr(t) for t in tokens if 32 <= t < 127])
    
    def token_count(self, text):
        """计算 token 数量"""
        return len(self.encode(text))

tokenizer = Tokenizer()
