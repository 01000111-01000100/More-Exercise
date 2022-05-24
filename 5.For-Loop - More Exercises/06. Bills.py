months = int(input())
water_bill = 20
internet_bill = 15
other_bills = 0

water_bills_cnt = 0
internet_bills_cnt = 0
electricity_bill_cnt = 0
other_bills_cnt = 0

for month in range(months):
    electricity_bill = float(input())

    electricity_bill_cnt += electricity_bill
    water_bills_cnt += water_bill
    internet_bills_cnt += internet_bill
    other_bills = (electricity_bill + water_bill + internet_bill) * 1.2
    other_bills_cnt += other_bills

average = (electricity_bill_cnt + water_bills_cnt + internet_bills_cnt + other_bills_cnt) / months

print(f"Electricity: {electricity_bill_cnt:.2f} lv")
print(f"Water: {water_bills_cnt:.2f} lv")
print(f"Internet: {internet_bills_cnt:.2f} lv")
print(f"Other: {other_bills_cnt:.2f} lv")
print(f"Average: {average:.2f} lv")
