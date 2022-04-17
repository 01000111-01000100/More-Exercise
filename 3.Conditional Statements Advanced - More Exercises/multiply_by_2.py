num = 0

while num >= 0:
    num = float(input())
    if num >= 0:
        num = num * 2
        print(f"Result: {num:.2f}")
    else:
        print("Negative number!")