# WatchAndyTW, 2024/10/25

import random

def main():
    # Roll dice for player
    # 玩家擲骰子
    player_dices = roll_dice()
    player_score = calc_score(player_dices)
    print("Player: {}, Score: {}".format(' '.join(str(x) for x in player_dices), player_score))
    # Roll dice for computer
    # 電腦擲骰子
    computer_dices = roll_dice()
    computer_score = calc_score(computer_dices)
    print("Computer: {}, Score: {}".format(' '.join(str(x) for x in computer_dices), computer_score))
    # Calculate result
    # 計算結果
    if player_score > computer_score:
        print("Player wins!")
    elif computer_score > player_score:
        print("Computer wins!")
    else:
        print("Draw!")

# Roll dice function
# 擲骰子函數
def roll_dice():
    dices = []
    for i in range(1,6):
        dices.append(random.randint(1, 6))
    return dices

# Calculate score function
# 計算分數函數
def calc_score(dices):
    score = 0
    for i in range(len(dices)):
        if int(dices[i]) == 3:
            continue
        score += int(dices[i])
    return score

main()

# 本檔案僅為公開交流使用
# This file is public for communication only
# https://github.com/WatchAndyTW/PythonHomework/blob/main/2024.10.24/413401120_HA2.py