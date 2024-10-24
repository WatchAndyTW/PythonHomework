# WatchAndyTW, 2024/10/25

import math

def main():
    # Get user inputs
    # 取得使用者輸入
    a = int(input("請輸入 a 參數："))
    b = int(input("請輸入 b 參數："))
    c = int(input("請輸入 c 參數："))
    # Calculation
    # 數學計算
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        print("x 為實根：")
        x1 = int((-b - math.sqrt(d)) / (2 * a))
        x2 = int((-b + math.sqrt(d)) / (2 * a))
        print("x = {}, {}".format(x1, x2))
    elif d == 0:
        print("x 為重根：")
        x = int(-b / (2 * a))
        print("x = {}".format(x))
    else:
        print("x 沒有實根")
        return

main()

# 本檔案僅為公開交流使用
# This file is public for communication only
# https://github.com/WatchAndyTW/PythonHomework/blob/main/2024.10.24/413401120_HA1.py