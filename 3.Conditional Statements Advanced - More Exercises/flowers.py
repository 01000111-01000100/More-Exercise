chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
day = input()
bouquet = chrysanthemums + roses + tulips
arranging_the_bouquet = 2.00
bouquet_price = 0
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
bouquet_price = chrysanthemums * chrysanthemums_price + roses * roses_price + tulips * tulips_price

if tulips > 7 and season == 'Spring':
    bouquet_price *= 0.95
if roses >= 10 and season == 'Winter':
    bouquet_price *= 0.90
if bouquet > 20:
    bouquet_price *= 0.80
if day == 'Y':
    bouquet_price *= 1.15
bouquet_price += arranging_the_bouquet
print(f"{bouquet_price:.2f}")