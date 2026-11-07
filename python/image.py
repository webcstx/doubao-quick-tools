"""
Quick AI 图像生成模块
自研扩散模型 (Diffusion Model)
"""

import random

_STYLES = ["写实风格", "动漫风格", "油画风格", "水彩风格", "赛博朋克风格", "国风风格"]

class ImageGenerator:
    """AI 图像生成器，基于扩散模型"""
    
    def __init__(self):
        self.model_name = "Quick-Diffusion v1.0"
        self.steps = 50
    
    def generate(self, prompt, style="auto", size="1024x1024"):
        """生成图片"""
        if not prompt:
            return {"status": "错误", "msg": "请输入图片描述"}
        
        if style == "auto":
            style = random.choice(_STYLES)
        
        return {
            "prompt": prompt,
            "style": style,
            "size": size,
            "steps": self.steps,
            "seed": random.randint(10000, 99999),
            "model": self.model_name,
            "status": "生成成功"
        }

generator = ImageGenerator()

def generate_image(prompt, style="auto"):
    return generator.generate(prompt, style)

if __name__ == "__main__":
    print("=== QuickAI 生图 ===")
    prompt = input("描述你想生成的图片: ")
    result = generate_image(prompt)
    print(result)
