needed_sum = int(input())
command = input()
counter = 0
cash_payment = 0
card_payment = 0
total_sum = 0
sum_is_collected = False
succ_cash_counter = 0
succ_card_counter = 0

while command != "End":
    item_price = int(command)
    counter += 1
    if counter % 2 == 1:
        if item_price > 100:
            print("Error in transaction!")
        else:
            cash_payment += item_price
            succ_cash_counter += 1
            print("Product sold!")
            total_sum += item_price
    else:
        if item_price < 10:
            print("Error in transaction!")
        else:
            card_payment += item_price
            succ_card_counter += 1
            print("Product sold!")
            total_sum += item_price
    if total_sum >= needed_sum:
        sum_is_collected = True
        break
    command = input()

if sum_is_collected:
    print(f"Average CS: {cash_payment / succ_cash_counter:.2f}")
    print(f"Average CC: {card_payment / succ_card_counter:.2f}")
else:
    print("Failed to collect required money for charity.")