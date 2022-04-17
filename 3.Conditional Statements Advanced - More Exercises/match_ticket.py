import math

budget = float(input())
category = str(input())
number_ppl_in_group = int(input())

ticket = 0
discount = " "
if category == "VIP":
    ticket += 499.99
    if number_ppl_in_group <= 4:
        discount = budget * 0.75
    elif number_ppl_in_group <= 9:
        discount = budget * 0.60
    elif number_ppl_in_group <= 24:
        discount = budget * 0.50
    elif number_ppl_in_group <= 49:
        discount = budget * 0.40
    elif number_ppl_in_group >= 50:
        discount = budget * 0.25
elif category == "Normal":
    ticket += 249.99
    if number_ppl_in_group <= 4:
        discount = budget * 0.75
    elif number_ppl_in_group <= 9:
        discount = budget * 0.60
    elif number_ppl_in_group <= 24:
        discount = budget * 0.50
    elif number_ppl_in_group <= 49:
        discount = budget * 0.40
    elif number_ppl_in_group >= 50:
        discount = budget * 0.25
budget_left = budget - discount
total_ticket = ticket * number_ppl_in_group
if total_ticket > budget_left:
    money_left = abs(budget_left - total_ticket)
    print(f"Not enough money! You need {money_left:.2f} leva.")
else:
    money_needed = abs(total_ticket - budget_left)
    print(f"Yes! You have {money_needed:.2f} leva left.")
