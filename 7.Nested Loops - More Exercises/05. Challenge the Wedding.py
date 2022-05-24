male = int(input())
female = int(input())
max_seats = int(input())
counter = 0
couples = ''

for i in range(1, male + 1):
    for j in range(1, female + 1):
        counter += 1
        couples += f'({i} <-> {j}) '
        if counter == max_seats:
            break
print(couples)