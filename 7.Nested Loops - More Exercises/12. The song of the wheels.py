num = int(input())
counter = 0
g = 1
h = 1
j = 1
k = 1

for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if num == a * b + c * d:
                    if a < b and c > d:
                        print(f"{a}{b}{c}{d}", end=' ')
                        counter += 1

                        if counter == 4:
                            g = a
                            h = b
                            j = c
                            k = d

if counter >= 4:
    print("")
    print(f"Password: {g}{h}{j}{k}", end=' ')
else:
    print("")
    print("No!")