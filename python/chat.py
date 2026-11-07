"""
Quick AI 聊天模块
基于 QuickAIModel 的对话接口
"""

from model import model
from tokenizer import tokenizer

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

import random

def chat(message):
    """与 AI 对话"""
    if not message:
        return "请输入你的问题哦～"
    
    # 调用模型推理
    inference = model.forward(message)
    
    if "你好" in message or "hi" in message.lower():
        return f"你好！很高兴见到你 😊 (推理耗时: {inference['inference_time_ms']}ms)"
    elif "模型" in message or "你是谁" in message:
        info = model.info()
        return f"我是 {info['name']} 大模型 v{info['version']}，架构是 {info['architecture']}，参数量 {info['parameters']}。"
    elif "名字" in message:
        return "我是QuickAI，你的智能助手！"
    elif "版本" in message:
        return f"我当前的版本是 v{model.version}"
    elif "谢谢" in message:
        return "不客气！有问题随时找我～"
    else:
        return random.choice(_RESPONSES)

if __name__ == "__main__":
    print("=== QuickAI 聊天 ===")
    print("模型已加载，输入 exit 退出")
    while True:
        msg = input("你: ")
        if msg.lower() == "exit":
            break
        print("AI:", chat(msg))
