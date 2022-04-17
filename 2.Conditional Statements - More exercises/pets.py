import math

days = int(input())
food_left_kg = int(input())
dogfood_per_day = float(input())
catfood_per_day = float(input())
turtlefood_per_day_gramms = float(input())

dog = days * dogfood_per_day
cat = days * catfood_per_day
turtle = days * turtlefood_per_day_gramms / 1000
total_food = dog + cat + turtle
if total_food <= food_left_kg:
    food_left = math.floor(food_left_kg - total_food)
    print(f"{food_left} kilos of food left.")
else:
    food_needed = math.ceil(total_food - food_left_kg)
    print(f"{food_needed} more kilos of food are needed.")