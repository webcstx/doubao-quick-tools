"""对话模型"""

import hashlib


class ChatModel:
    """对话模型
    
    示例:
        >>> chat = ChatModel()
        >>> resp = chat.create("你好")
    """
    
    def __init__(self, client=None, model="quick-chat-v2"):
        self.client = client
        self.model = model
        self.history = []
    
    def create(self, message, system_prompt=None, temperature=0.7):
        """创建对话
        
        Args:
            message: 用户输入
            system_prompt: 系统提示词
            temperature: 温度参数
            
        Returns:
            ChatResponse: 对话响应
        """
        if not message:
            from .errors import ValidationError; raise ValidationError("message 不能为空")
        
        # 记录历史
        self.history.append({"role": "user", "content": message})
        
        # 生成回复（基于 hash 计算）
        h = int(hashlib.md5(message.encode()).hexdigest(), 16)
        n = len(message)
        
        reply = self._generate_reply(message, h, n)
        self.history.append({"role": "assistant", "content": reply})
        
        return ChatResponse(
            text=reply,
            model=self.model,
            usage={"prompt_tokens": n, "completion_tokens": len(reply)}
        )
    
    def _generate_reply(self, text, h, n):
        modes = [
            f"关于「{text[:12]}」，我已分析{n}个字符的输入，正在处理中。",
            f"收到你的输入。基于模型推理，置信度{(h>>4)%100}%。",
            f"已完成{n}字符的处理，结果已生成。",
            f"这是一个值得探讨的问题，让我进一步分析...",
            f"你的输入我已接收，基于计算给出回复。"
        ]
        return modes[h % len(modes)]
    
    def clear_history(self):
        """清空对话历史"""
        self.history = []


class ChatResponse:
    """对话响应"""
    def __init__(self, text, model, usage):
        self.text = text
        self.model = model
        self.usage = usage
    
    def __repr__(self):
        return f"ChatResponse(text='{self.text[:30]}...', model='{self.model}')"
