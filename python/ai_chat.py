"""
Quick AI 聊天模块
自研轻量级 AI 对话引擎
"""

import random

_RESPONSES = [
    "你好呀！我是QuickAI，有什么可以帮你的吗？",
    "这是个好问题！让我想想...",
    "我明白你的意思了，我们可以这样做：",
    "很棒的想法！继续说说看？",
    "嗯嗯，我理解了。还有其他问题吗？",
    "作为AI助手，我建议你试试这个方法：",
    "这个问题我刚好知道答案！",
    "让我来帮你分析一下这个问题。",
]

def chat(message):
    if not message:
        return "请输入你的问题哦～"
    if "你好" in message or "hi" in message.lower():
        return "你好！很高兴见到你 😊"
    elif "名字" in message:
        return "我是QuickAI，你的智能助手！"
    elif "模型" in message or "你是谁" in message or "什么AI" in message:
        return "我是 Quick AI 大模型 v2.0.0，一个自研的轻量级 AI 引擎，支持聊天和图片生成功能。"
    elif "版本" in message:
        return "我当前的版本是 v2.0.0"
    elif "谢谢" in message:
        return "不客气！有问题随时找我～"
    else:
        return random.choice(_RESPONSES)

if __name__ == "__main__":
    print("=== QuickAI 聊天 ===")
    while True:
        msg = input("你: ")
        if msg.lower() == "exit":
            break
        print("AI:", chat(msg))
