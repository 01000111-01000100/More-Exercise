import math

first_pair = int(input())
second_pair = int(input())
first_diff = int(input())
second_diff = int(input())

for first in range(first_pair, first_pair + first_diff + 1):
    for second in range(second_pair, second_pair + second_diff + 1):
        first_sqrt = int(math.floor(math.sqrt(first)))
        second_sqrt = int(math.floor(math.sqrt(second)))
        is_prime1 = True
        is_prime2 = True

        for first1 in range(2, first_sqrt + 1):
            if first % first1 == 0:
                is_prime1 = False
        for second2 in range(2, second_sqrt + 1):
            if second % second2 == 0:
                is_prime2 = False
        if is_prime1 == True and is_prime2 == True:
            print(f"{first}{second}")