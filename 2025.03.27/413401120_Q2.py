# WatchAndyTW, 2025/03/27

def main(text: str):
    text = list(map(int, text.split(" ")))
    mid = len(text) // 2
    front = sum(text[:mid])
    back = sum(text[mid:])
    print("天秤傾左") if front > back else print("天秤保持水平") if front == back else print("天秤傾右")

main(str(input("請輸入測資：")))