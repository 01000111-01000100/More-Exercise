offdays = int(input())
if ((365 - offdays) * 63 + offdays * 127) > 30000:
    print(f"Tom will run away\n{((365 - offdays) * 63 + offdays * 127-30000)//60} hours and {((365 - offdays) * 63 + offdays * 127-30000)%60} minutes more for play")
else:
    print(f"Tom sleeps well\n{(30000-((365 - offdays) * 63 + offdays * 127))//60} hours and {(30000-((365 - offdays) * 63 + offdays * 127))%60} minutes less for play")