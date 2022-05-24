n_number = int(input())
l_number = int(input())

for i1 in range(1, n_number + 1):
    for i2 in range(1, n_number + 1):
        for i3 in range(97, l_number + 97):
            for i4 in range(97, l_number + 97):
                for i5 in range(2, n_number + 1):
                    if i5 > i1 and i5 > i2:
                        print(f"{i1}{i2}{chr(i3)}{chr(i4)}{i5}", end=' ')