#!/usr/bin/env python3
"""文本反转工具"""
def reverse_text(text):
    return text[::-1]

if __name__ == "__main__":
    text = input("输入要反转的文本: ")
    print(f"反转结果: {reverse_text(text)}")
