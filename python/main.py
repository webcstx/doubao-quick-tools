"""
Quick AI 大模型 v2.0.0
自研轻量级 AI 引擎，支持聊天和生图
"""

from model import model
from chat import chat
from image import generate_image

def main():
    print("=" * 50)
    print("🤖 Quick AI 大模型 v2.0.0")
    info = model.info()
    print(f"   架构: {info['architecture']}")
    print(f"   参数量: {info['parameters']}")
    print("=" * 50)
    print()
    print("功能：")
    print("1. AI 聊天对话")
    print("2. AI 生成图片")
    print("3. 模型信息")
    print("4. 退出")
    print()
    
    while True:
        choice = input("请选择 (1/2/3/4): ")
        
        if choice == "1":
            print("\n--- AI 聊天 ---")
            msg = input("你: ")
            print("AI:", chat(msg))
            print()
        
        elif choice == "2":
            print("\n--- AI 生图 ---")
            prompt = input("图片描述: ")
            result = generate_image(prompt)
            print("生成结果:")
            for k, v in result.items():
                print(f"  {k}: {v}")
            print()
        
        elif choice == "3":
            print("\n--- 模型信息 ---")
            info = model.info()
            for k, v in info.items():
                print(f"  {k}: {v}")
            print()
        
        elif choice == "4":
            print("再见！👋")
            break
        
        else:
            print("请输入 1、2、3 或 4")

if __name__ == "__main__":
    main()
