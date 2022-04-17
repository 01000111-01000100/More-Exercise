import math
yard = int(input())
grapes_kg = float(input())
wine = int(input())
workers = int(input())
total_grapes = yard * grapes_kg
wine_made = 0.4 * total_grapes / 2.5
wine_for_workers = abs(wine_made - wine)
if wine_made >= wine:
    wine_per_person = (wine_made - wine) / workers
    print(f"Good harvest this year! Total wine: {math.floor(wine_made)} liters.")
    print(f"{math.ceil(wine_for_workers)} liters left -> {math.ceil(wine_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(wine_for_workers)} liters wine needed.")