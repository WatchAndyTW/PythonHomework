import random
import re

pattern = re.compile("^[a-z]+$")
answer_list = ["apple", "banana", "kiwi"]
show_char_list = []

def main():
    answer = random.choice(answer_list)
    print(f'題目：{"".join("-" for _ in range(len(answer)))}')
    win = False
    for i in range(5):
        print(f"========== Round {i + 1} ==========")
        char = ask_for_char()
        show_char_list.append(char)
        print_text = "".join(x if x in show_char_list else "-" for x in answer)
        if print_text == answer:
            win = True
            break
        print(f'當前狀態：{"".join(x if x in show_char_list else "-" for x in answer)}')
    print(f"=============================")
    print("".join(f"你猜對了！答案是：{answer}！" if win else f"遊戲失敗！正確答案是：{answer}！"))

def ask_for_char():
    char = input("請輸入一個英文字母：")
    if len(char) > 1:
        print("輸入錯誤，請重新輸入一個英文字母。")
        char = ask_for_char()
    elif not pattern.match(char):
        print("輸入錯誤，請重新輸入一個英文字母。")
        char = ask_for_char()
    elif char in answer_list:
        print("輸入錯誤，請重新輸入一個英文字母。")
        char = ask_for_char()
    return char

main()