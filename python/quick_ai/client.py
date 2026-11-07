"""Quick AI 客户端"""

from .chat import ChatModel
from .image import ImageModel
from .embedding import EmbeddingModel
from .config import DEFAULT_CONFIG


class QuickAIClient:
    """Quick AI 主客户端
    
    示例:
        >>> client = QuickAIClient()
        >>> resp = client.chat.create("你好")
        >>> print(resp.text)
    """
    
    def __init__(self, api_key=None, base_url=None, **kwargs):
        self.api_key = api_key or "quick-local"
        self.base_url = base_url or DEFAULT_CONFIG["base_url"]
        
        # 初始化各模型模块
        self.chat = ChatModel(client=self)
        self.image = ImageModel(client=self)
        self.embedding = EmbeddingModel(client=self)
    
    def list_models(self):
        """列出支持的模型"""
        return [
            {"id": "quick-chat-v2", "name": "Quick Chat", "type": "chat"},
            {"id": "quick-image-v2", "name": "Quick Image", "type": "image"},
            {"id": "quick-embed-v2", "name": "Quick Embedding", "type": "embedding"},
        ]
    
    def __repr__(self):
        return f"QuickAIClient(base_url='{self.base_url}')"
