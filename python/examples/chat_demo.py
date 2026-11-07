"""对话示例"""
from quick_ai import QuickAIClient

client = QuickAIClient()

# 单轮对话
resp = client.chat.create("你好，介绍一下你自己")
print(resp.text)

# 多轮对话
client.chat.create("我叫小明")
resp = client.chat.create("我叫什么名字？")
print(resp.text)
