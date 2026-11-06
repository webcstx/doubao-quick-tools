#!/usr/bin/env python3
"""时间转换器 - 当前时间/时间戳互相转换"""
import time
from datetime import datetime

def show_now():
    now = datetime.now()
    ts = int(time.time())
    print(f"当前本地时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"当前时间戳:   {ts}")

def ts_to_time(ts):
    try:
        dt = datetime.fromtimestamp(int(ts))
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except:
        return "无效的时间戳"

def time_to_ts(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return int(dt.timestamp())
    except:
        return "格式错误，请用 YYYY-MM-DD HH:MM:SS"

if __name__ == "__main__":
    print("=== 时间转换器 ===")
    show_now()
    print()
    
    ts = input("输入时间戳转时间（直接回车跳过）: ")
    if ts.strip():
        print(f"转换结果: {ts_to_time(ts)}")
    
    ds = input("输入时间转时间戳（YYYY-MM-DD HH:MM:SS）: ")
    if ds.strip():
        print(f"转换结果: {time_to_ts(ds)}")
