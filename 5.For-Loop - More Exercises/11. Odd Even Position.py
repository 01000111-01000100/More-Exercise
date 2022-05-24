n = int(input())
sumOdd = 0
sumEven = 0
maxOdd = -555555555
maxEven = -555555555
minOdd = 555555555
minEven = 555555555
i = 1
while i <= n:
    number = float(input())
    if i % 2 == 0:
        sumEven += number
        if number > maxEven:
            maxEven = number
        if number < minEven:
            minEven = number
    else:
        sumOdd += number
        if number > maxOdd:
            maxOdd = number
        if number < minOdd:
            minOdd = number
    i += 1
print(f"OddSum={sumOdd:.2f},")
if minOdd != 555555555:
    print(f"OddMin={minOdd:.2f},")
else:
    print("OddMin=No,")
if maxOdd != -555555555:
    print(f"OddMax={maxOdd:.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={sumEven:.2f},")
if minEven != 555555555:
    print(f"EvenMin={minEven:.2f},")
else:
    print("EvenMin=No,")
if maxEven != -555555555:
    print(f"EvenMax={maxEven:.2f}")
else:
    print("EvenMax=No")
