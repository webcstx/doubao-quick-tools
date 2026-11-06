#!/usr/bin/env python3
"""阿拉伯数字转中文"""
def num_to_chinese(num):
    digits = "零一二三四五六七八九"
    units = ["", "十", "百", "千", "万", "十", "百", "千", "亿"]
    s = str(num)
    result = ""
    n = len(s)
    for i, d in enumerate(s):
        d = int(d)
        if d != 0:
            result += digits[d] + units[n - 1 - i]
        else:
            if result and not result.endswith("零"):
                result += "零"
    return result.rstrip("零")

if __name__ == "__main__":
    num = input("输入数字: ")
    print(f"中文: {num_to_chinese(num)}")
