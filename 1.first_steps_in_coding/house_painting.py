x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 1.5 * 1.5
both_side = 2 * side_wall - 2 * window
back_side = x * x
door = 1.2 * 2
front_back_side = 2 * back_side - door
total_plosht = both_side + front_back_side
green_color = total_plosht / 3.4

pokriv_prav = 2 * (x * y)
pokriv_tri = 2 * (x * h / 2)

total_pokriv = pokriv_prav + pokriv_tri
red_color = total_pokriv / 4.3

print(f"{green_color:.2f}")
print(f"{red_color:.2f}")