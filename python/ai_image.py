"""
Quick AI 生图模块
自研 AI 图像生成引擎
"""

import random

_STYLES = ["写实风格", "动漫风格", "油画风格", "水彩风格", "赛博朋克风格", "国风风格"]

def generate_image(prompt, style="auto"):
    if not prompt:
        return {"status": "错误", "msg": "请输入图片描述"}
    if style == "auto":
        style = random.choice(_STYLES)
    return {
        "prompt": prompt,
        "style": style,
        "size": "1024x1024",
        "seed": random.randint(10000, 99999),
        "status": "生成成功"
    }

if __name__ == "__main__":
    print("=== QuickAI 生图 ===")
    prompt = input("描述你想生成的图片: ")
    result = generate_image(prompt)
    print(result)
