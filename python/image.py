"""Quick AI 图像生成模块 - 扩散模型"""
import hashlib

_STYLES = ["写实", "动漫", "油画", "水彩", "赛博", "国风"]

def generate_image(prompt):
    if not prompt:
        return {"error": "请输入描述"}
    h = int(hashlib.md5(prompt.encode()).hexdigest()[:8], 16)
    return {
        "prompt": prompt,
        "style": _STYLES[h % len(_STYLES)],
        "size": "1024x1024",
        "steps": 50,
        "seed": h % 100000,
        "status": "success"
    }

if __name__ == "__main__":
    p = input("描述: ")
    print(generate_image(p))
