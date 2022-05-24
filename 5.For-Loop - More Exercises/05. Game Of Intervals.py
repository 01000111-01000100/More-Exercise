number = int(input())

procent_0_9 = 0
procent_10_19 = 0
procent_20_29 = 0
procent_30_39 = 0
procent_40_50 = 0
procent_invalid = 0

points = 0
for num in range(number):
    new_number = int(input())
    if 40 <= new_number <= 50:
        points += 100
        procent_40_50 += 1

    elif 30 <= new_number <= 39:
        points += 50
        procent_30_39 += 1

    elif 20 <= new_number <= 29:
        points += new_number * 0.4
        procent_20_29 += 1

    elif 10 <= new_number <= 19:
        points += new_number * 0.3
        procent_10_19 += 1

    elif 0 <= new_number <= 9:
        points += new_number * 0.2
        procent_0_9 += 1

    else:
        points = points / 2
        procent_invalid += 1

percent_0to9 = (procent_0_9 / number) * 100
percent_10to19 = (procent_10_19 / number) * 100
percent_20to29 = (procent_20_29 / number) * 100
percent_30to39 = (procent_30_39 / number) * 100
percent_40to50 = (procent_40_50 / number) * 100
percent_invalid = (procent_invalid / number) * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percent_0to9:.2f}%")
print(f"From 10 to 19: {percent_10to19:.2f}%")
print(f"From 20 to 29: {percent_20to29:.2f}%")
print(f"From 30 to 39: {percent_30to39:.2f}%")
print(f"From 40 to 50: {percent_40to50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
