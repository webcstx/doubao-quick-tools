#!/usr/bin/env python3
"""Base64 编解码工具"""
import base64

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    try:
        return base64.b64decode(text).decode()
    except:
        return "解码失败"

if __name__ == "__main__":
    text = input("输入要编码的文本: ")
    print(f"编码结果: {encode(text)}")
    code = input("输入要解码的Base64: ")
    print(f"解码结果: {decode(code)}")
