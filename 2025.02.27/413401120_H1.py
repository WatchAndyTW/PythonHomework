# WatchAndyTW, 2025/02/27

def factor_number_generator():
    num = int(input("Enter a number: "))
    print([x for x in range(1, num + 1) if num % x == 0])

factor_number_generator()