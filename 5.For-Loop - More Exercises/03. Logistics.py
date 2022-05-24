the_num_of_cargo = int(input())
price_minibus = 0
price_truck = 0
price_train = 0
sum_cargo_minibus = 0
sum_cargo_truck = 0
sum_cargo_train = 0
sum_cargo = 0
for i in range(1, the_num_of_cargo + 1):
    the_ton_of_cargo = int(input())
    sum_cargo += the_ton_of_cargo
    if the_ton_of_cargo <= 3:
        sum_cargo_minibus += the_ton_of_cargo
        price_minibus += the_ton_of_cargo * 200
    elif the_ton_of_cargo <= 11:
        sum_cargo_truck += the_ton_of_cargo
        price_truck += the_ton_of_cargo * 175
    elif the_ton_of_cargo > 11:
        sum_cargo_train = the_ton_of_cargo
        price_train = the_ton_of_cargo * 120

sum_average_price = (price_minibus + price_truck + price_train) / sum_cargo
percent_mini_bus = sum_cargo_minibus / sum_cargo * 100
percent_truck = sum_cargo_truck / sum_cargo * 100
percent_train = sum_cargo_train / sum_cargo * 100
print(f"{sum_average_price:.2f}")
print(f"{percent_mini_bus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")