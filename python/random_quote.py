#!/usr/bin/env python3
"""随机励志名言"""
import random

quotes = [
    "千里之行，始于足下。",
    "学而不思则罔，思而不学则殆。",
    "天行健，君子以自强不息。",
    "书山有路勤为径，学海无涯苦作舟。",
    "失败乃成功之母。",
    "只要功夫深，铁杵磨成针。",
]

if __name__ == "__main__":
    print(random.choice(quotes))
