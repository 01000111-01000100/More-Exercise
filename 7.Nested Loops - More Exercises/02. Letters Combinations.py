first_letter = input()
second_letter = input()
third_letter = input()
counter = 0
for i in range(ord(first_letter), ord(second_letter) + 1):
    for j in range(ord(first_letter), ord(second_letter) + 1):
        for k in range(ord(first_letter), ord(second_letter) + 1):
            if ord(third_letter) != i and ord(third_letter) != j and ord(third_letter) != k:
                counter += 1
                print(f"{chr(i)}{chr(j)}{chr(k)} ", end="")

print(f"{counter}")