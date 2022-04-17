season = input()
km_mounth = float(input())
price_spring_aut = 0
price_summer = 0
price_winter = 0
all_price = 0
price_km = 0
total = 0
if km_mounth <= 5000:
    if season == "Spring" or season == "Autumn":
        price_spring_aut = 0.75
        price_km = (price_spring_aut * km_mounth) * 4
        total = price_km - (price_km * 0.10)
    elif season == "Summer":
        price_summer = 0.90
        price_km = (price_summer * km_mounth) * 4
        total = price_km - (price_km * 0.10)
    elif season == "Winter":
        price_winter = 1.05
        price_km = (price_winter * km_mounth) * 4
        total = price_km - (price_km * 0.10)

if 5000 < km_mounth <= 10000:
    if season == "Spring" or season == "Autumn":
        price_spring_aut = 0.95
        price_km = (price_spring_aut * km_mounth) * 4
        total = price_km - (price_km * 0.10)
    elif season == "Summer":
        price_summer = 1.10
        price_km = (price_summer * km_mounth) * 4
        total = price_km - (price_km * 0.10)
    elif season == "Winter":
        price_winter = 1.25
        price_km = (price_winter * km_mounth) * 4
        total = price_km - (price_km * 0.10)

if 10000 < km_mounth <= 20000:
    if season == "Spring" or season == "Summer" or season == "Autumn" or season == "Winter":
        all_price = 1.45
        price_km = (all_price * km_mounth) * 4
        total = price_km - (price_km * 0.10)

print(f"{total:.2f}")