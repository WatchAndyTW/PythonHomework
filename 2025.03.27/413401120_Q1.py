# WatchAndyTW, 2025/03/27

print("".join([x.upper() if x.islower() else chr(((ord(x) - ord('A') + 3) % 26) + ord('A')) for x in reversed(str(input("請輸入測資：")))]))