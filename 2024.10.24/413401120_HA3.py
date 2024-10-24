# WatchAndyTW, 2024/10/25

import random

def main():
    # Define variables
    # 宣告變數
    cardinality = 0
    even = 0
    rolled = []
    red_gk_money = 0
    stop_red_gk = False
    black_gk_money = 0
    stop_black_gk = False
    multiplier = 0
    while True:
        # Increase multiplier
        # 增加乘數
        multiplier += 1
        # Roll dice
        # 擲骰子
        dice = roll_dice()
        # Increase counter if the number wasn't rolled before
        # 如果之前沒有骰到過這個數字，增加計數器
        if dice not in rolled:
            if dice % 2 == 0:
                even += 1
            else:
                cardinality += 1
        # Append number to list
        # 將數字加入列表中
        rolled.append(dice)
        # Check if GK met
        # 檢查 GK 是否達到
        if cardinality == 3 and not stop_black_gk:
            stop_black_gk = True
            black_gk_money = multiplier * 100
        if even == 3 and not stop_red_gk:
            stop_red_gk = True
            red_gk_money = multiplier * 100
        # Stop the loop if met the condition
        # 如果達到條件則停止循環
        if cardinality == 3 and even == 3:
            break
    # Print result
    # 顯示結果
    print(' '.join(str(x) for x in rolled))
    print("總花費：{}".format(multiplier * 100))
    for i in range(1, 7):
        x = 0
        for j in rolled:
            if i == j:
                x += 1
        print("+{} 點小賞：{} 個".format(i, x))
    print("得到紅 GK 時的花費：{}".format(red_gk_money))
    print("得到黑 GK 時的花費：{}".format(black_gk_money))

# Roll dice function
# 擲骰子函數
def roll_dice():
    return random.randint(1, 6)

main()

# 本檔案僅為公開交流使用
# This file is public for communication only
# https://github.com/WatchAndyTW/PythonHomework/blob/main/2024.10.24/413401120_HA3.py