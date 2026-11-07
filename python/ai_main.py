"""
豆包 AI 大模型 v2.0.0
自研轻量级 AI 引擎，支持聊天和生图
"""

from ai_chat import chat
from ai_image import generate_image

def main():
    print("=" * 40)
    print("🤖 豆包 AI 大模型 v2.0.0")
    print("=" * 40)
    while True:
        choice = input("\n1=聊天 2=生图 3=退出: ")
        if choice == "1":
            msg = input("你: ")
            print("AI:", chat(msg))
        elif choice == "2":
            prompt = input("图片描述: ")
            print("生成结果:", generate_image(prompt))
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
