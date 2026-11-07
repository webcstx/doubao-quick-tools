"""工具函数"""

import hashlib
import time


def compute_hash(text):
    """计算文本 hash"""
    return hashlib.md5(text.encode()).hexdigest()


def timestamp():
    """当前时间戳"""
    return int(time.time())


def truncate(text, max_len=100):
    """截断文本"""
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."
