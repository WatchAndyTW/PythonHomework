# WatchAndyTW, 2024/10/25

def main():
    # Get user input IC
    # 取得使用者輸入之全年綜合所得
    ic = int(input("請輸入全年綜合所得（元）："))
    # Calculate NIC
    # 計算全年綜合所得淨額
    nic = ic - 300000
    # Check for NIC
    # 檢測全年綜合所得淨額
    if nic > 0:
        # Make the number smaller for better coding experience
        # 把數字簡化以利編寫
        nic_small = nic / 10000
        # Default to 5%
        # 預設乘數為 5%
        multiplier = 0.05
        if 54 < nic_small <= 121:
            multiplier = 0.12
        elif 121 < nic_small <= 242:
            multiplier = 0.20
        elif 242 < nic_small <= 453:
            multiplier = 0.30
        elif nic_small > 453:
            multiplier = 0.40
        # Calculate tax
        # 計算所得稅
        tax = nic * multiplier
        # Print result
        # 顯示結果
        print("今年的所得稅為：{}".format(tax))
    else:
        # Print result
        # 顯示結果
        print("今年的所得稅為：0")
        print("月平均可支用所得為：{}".format(ic / 12))

main()

# 本檔案僅為公開交流使用
# This file is public for communication only
# https://github.com/WatchAndyTW/PythonHomework/blob/main/2024.10.24/413401120_HA0.py