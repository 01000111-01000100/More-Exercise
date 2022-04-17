pro_kg_veg = float(input())
pro_kg_fruit = float(input())
kg_veg = int(input())
kg_fruit = int(input())
veggies = pro_kg_veg * kg_veg
fruits = pro_kg_fruit * kg_fruit
shop = (veggies + fruits) / 1.94
print(f"{shop:.2f}")

