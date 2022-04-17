import math

magnoli = int(input())
zumbuli = int(input())
rozi = int(input())
kaktusi = int(input())
gift_price = float(input())

sum = magnoli * 3.25 + zumbuli * 4 + rozi * 3.5 + kaktusi * 8
taxes = sum * 0.05
sum = sum - taxes
needed_sum = math.floor(sum - gift_price)
left_sum = math.ceil(gift_price - sum)
if gift_price > sum:
    print(f"She will have to borrow {left_sum} leva.")
else:
    print(f"She is left with {needed_sum} leva.")