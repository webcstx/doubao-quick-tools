#!/usr/bin/env python3
"""随机密码生成器"""
import random
import string

def generate_password(length=12, use_upper=True, use_digit=True, use_symbol=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digit:
        chars += string.digits
    if use_symbol:
        chars += "!@#$%^&*()_+-=[]{}"
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    pwd = generate_password(16)
    print(f"生成的密码: {pwd}")
