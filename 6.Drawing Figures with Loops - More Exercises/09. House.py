import math

n = int(input())

stars = 1
if n % 2 == 0:
    stars += 1

roof_length = math.ceil(n / 2)
for roof_length in range((n + 1) // 2):
    padding = (n - stars) // 2
    line = '-' * padding \
           + '*' * stars \
           + '-' * padding
    print(line)
    stars += 2

for i in range(n // 2):
    line = '|' + '*' * (n - 2) + '|'
    print(line)
print()
