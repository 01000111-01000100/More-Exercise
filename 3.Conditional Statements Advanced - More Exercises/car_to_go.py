budget = float(input())
season = input()

class_car = ""
type_car = ""
price = 0
# First enter classes
if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.80
elif budget > 500:
    class_car = "Luxury class"
    if season == "Summer":
        type_car = "Jeep"
        price = budget * 0.90
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.90
print(f'{class_car}')
print(f'{type_car} - {price:.2f}')