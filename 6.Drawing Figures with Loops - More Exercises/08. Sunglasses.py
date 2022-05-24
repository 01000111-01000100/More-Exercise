import math

n = int(input())  # 3<n<100
width = 5 * n
upper_and_lower_rows = middle_row = spaces = stars = pipes = slashes = ""
for i in range(0, n):
    stars += "*"
    spaces += " "

upper_and_lower_rows += stars + stars + spaces + stars + stars
print(upper_and_lower_rows)
for a in range(0, n - 2):
    slashes = pipes = ""
    for i in range(0, n - 1):
        slashes += "/"
    slashes += slashes
    for i in range(0, n):
        if a == math.floor((n - 1) / 2 - 1):
            pipes += "|"
        else:
            pipes += " "
    middle_row = "*" + slashes + "*" + pipes + "*" + slashes + "*"
    print(middle_row)

print(upper_and_lower_rows)