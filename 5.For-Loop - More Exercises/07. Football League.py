stadium_capacity = int(input())
number_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
total_fans = 0

for fans in range(number_fans):
    fans_in_sector = input().upper()
    total_fans += 1
    if fans_in_sector == "A":
        sector_a += 1

    elif fans_in_sector == "B":
        sector_b += 1

    elif fans_in_sector == "V":
        sector_v += 1

    elif fans_in_sector == "G":
        sector_g += 1

percent_a = sector_a / number_fans * 100
percent_b = sector_b / number_fans * 100
percent_v = sector_v / number_fans * 100
percent_g = sector_g / number_fans * 100
percent_total_fans = number_fans / stadium_capacity * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_total_fans:.2f}%")