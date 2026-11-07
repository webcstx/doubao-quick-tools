"""Quick AI 大模型 v2.0.0"""
from model import model
from chat import chat
from image import generate_image

def main():
    print("=" * 40)
    print("Quick AI 大模型 v2.0.0")
    info = model.info()
    print(f"架构: {info['arch']} | 参数: {info['params']}")
    print("=" * 40)
    while True:
        c = input("\n1=聊天 2=生图 3=信息 4=退出: ")
        if c == "1":
            msg = input("你: ")
            print("AI:", chat(msg))
        elif c == "2":
            p = input("描述: ")
            print(generate_image(p))
        elif c == "3":
            for k, v in model.info().items():
                print(f"  {k}: {v}")
        elif c == "4":
            break

if __name__ == "__main__":
    main()
