grade = float(input())

if 5 <= grade < 12:
    print("Cold")
elif 12 < grade < 15:
    print("Cool")
elif 15 <= grade <= 20:
    print("Mild")
elif 20 < grade < 26:
    print("Warm")
elif 26 <= grade <= 35:
    print("Hot")
else:
    print("unknown")