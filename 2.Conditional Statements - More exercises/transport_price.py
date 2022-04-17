trip = int(input())
time = input().lower()

if trip < 20:
    if time == 'day':
        print('{taxi:.2f}'.format(taxi=0.7 + (trip * 0.79)))
    elif time == 'night':
        print('{taxi:.2f}'.format(taxi=0.7 + (trip * 0.90)))

if 20 <= trip < 100:
    print('{bus:.2f}'.format(bus=trip * 0.09))
elif 100 <= trip:
    print('{train:.2f}'.format(train=trip * 0.06))