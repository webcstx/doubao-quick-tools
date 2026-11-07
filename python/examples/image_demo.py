"""生图示例"""
from quick_ai import QuickAIClient

client = QuickAIClient()

resp = client.image.generate("一只在月光下的猫", style="国风")
print(f"风格: {resp.style}")
print(f"尺寸: {resp.size}")
print(f"种子: {resp.seed}")
