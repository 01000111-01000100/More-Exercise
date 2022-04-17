budget = float(input())
season = input()

destination = ""
type_house = ""
price = 0
if budget <= 1000:
    type_house = "Camp"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        destination = "Morocco"
        price = budget * 0.45

if 1000 < budget <= 3000:
    type_house = "Hut"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        destination = "Morocco"
        price = budget * 0.60

if budget > 3000:
    type_house = "Hotel"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        destination = "Morocco"
    price = budget * 0.90

print(f"{destination} - {type_house} - {price:.2f}")