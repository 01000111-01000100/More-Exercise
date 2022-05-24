one_lev_coins = int(input())
two_lev_coins = int(input())
five_lev_coins = int(input())
sum = int(input())
current_sum = 0

for one in range(0, one_lev_coins + 1):
    for two in range(0, two_lev_coins + 1):
        for five in range(0, five_lev_coins + 1):
            if one * 1 + two * 2 + five * 5 == sum:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {sum} lv.")