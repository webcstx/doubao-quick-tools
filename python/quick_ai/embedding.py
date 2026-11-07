"""向量嵌入模型"""

import hashlib


class EmbeddingModel:
    """向量嵌入模型
    
    示例:
        >>> emb = EmbeddingModel()
        >>> vec = emb.embed("你好")
    """
    
    def __init__(self, client=None, model="quick-embed-v2", dim=512):
        self.client = client
        self.model = model
        self.dim = dim
    
    def embed(self, text):
        """生成文本向量"""
        if not text:
            from .errors import ValidationError; raise ValidationError("text 不能为空")
        
        # 基于 hash 生成确定性向量
        h = int(hashlib.md5(text.encode()).hexdigest(), 16)
        vector = [(h >> i) % 100 / 100 for i in range(self.dim)]
        
        return EmbeddingResponse(
            text=text,
            vector=vector,
            dim=self.dim,
            model=self.model
        )


class EmbeddingResponse:
    """向量响应"""
    def __init__(self, text, vector, dim, model):
        self.text = text
        self.vector = vector
        self.dim = dim
        self.model = model
    
    def __repr__(self):
        return f"EmbeddingResponse(dim={self.dim}, model='{self.model}')"
