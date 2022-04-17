lenght = float(input())
widt = float(input())
cmlenght = lenght * 100
cmwwidt = widt * 100
miss_desks = 3
result = int(cmlenght / 120) * int((cmwwidt - 100) / 70) - miss_desks
print(result)