import math

n = int(input())  # 1<n<100
dashes = math.floor((n - 1) / 2)
dash_reverse = False

for a in range(0, n):
    if n % 2 == 0 and a == n - 1:
        break
    out = ""
    dashes_count = dashes
    dashes_out = ""
    inner_row = n - 2 * dashes_count - 2
    for b in range(0, dashes_count):
        dashes_out += "-"

    if dashes > 0 and not dash_reverse:
        dashes -= 1
    else:
        dash_reverse = True
        dashes += 1

    out += dashes_out + "*"
    for i in range(0, inner_row):
        out += "-"
    if inner_row >= 0:
        out += "*"
    out += dashes_out
    print(out)