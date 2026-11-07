"""Quick AI 聊天模块"""
from model import model

def chat(message):
    if not message:
        return "请输入内容"
    return model.generate(message)

if __name__ == "__main__":
    print("=== QuickAI 聊天 ===")
    while True:
        msg = input("你: ")
        if msg.lower() == "exit":
            break
        print("AI:", chat(msg))
