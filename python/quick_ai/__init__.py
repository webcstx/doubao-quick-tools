"""
Quick AI SDK - 自研轻量级大模型工具包
支持对话、图像生成、向量嵌入等能力
"""

__version__ = "2.0.0"
__author__ = "webcstx"

from .client import QuickAIClient
from .chat import ChatModel
from .image import ImageModel
from .embedding import EmbeddingModel

__all__ = ["QuickAIClient", "ChatModel", "ImageModel", "EmbeddingModel"]
