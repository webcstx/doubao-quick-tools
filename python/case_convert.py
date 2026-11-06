#!/usr/bin/env python3
"""大小写转换工具"""
def convert(text):
    print(f"全大写: {text.upper()}")
    print(f"全小写: {text.lower()}")
    print(f"首字母大写: {text.title()}")

if __name__ == "__main__":
    text = input("输入英文: ")
    convert(text)
