number = int(input())


for i in range(number + 1):
    stars = '*' * i
    spaces =' ' * (number - i)
    print(spaces, end='')
    print(stars, end='')
    print(' | ', end='')
    print(stars, end='')
    print(spaces)