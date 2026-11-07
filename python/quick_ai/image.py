"""图像生成模型"""

import hashlib


_STYLES = ["写实风格", "动漫风格", "油画风格", "水彩风格", "赛博朋克", "国风"]


class ImageModel:
    """图像生成模型
    
    示例:
        >>> img = ImageModel()
        >>> resp = img.generate("一只猫")
    """
    
    def __init__(self, client=None, model="quick-image-v2"):
        self.client = client
        self.model = model
    
    def generate(self, prompt, size="1024x1024", style="auto", n=1):
        """生成图像
        
        Args:
            prompt: 图像描述
            size: 尺寸
            style: 风格
            n: 生成数量
        """
        if not prompt:
            from .errors import ValidationError; raise ValidationError("prompt 不能为空")
        
        h = int(hashlib.md5(prompt.encode()).hexdigest()[:8], 16)
        
        if style == "auto":
            style = _STYLES[h % len(_STYLES)]
        
        return ImageResponse(
            prompt=prompt,
            style=style,
            size=size,
            seed=h % 100000,
            model=self.model
        )


class ImageResponse:
    """图像响应"""
    def __init__(self, prompt, style, size, seed, model):
        self.prompt = prompt
        self.style = style
        self.size = size
        self.seed = seed
        self.model = model
    
    def __repr__(self):
        return f"ImageResponse(prompt='{self.prompt}', style='{self.style}')"
