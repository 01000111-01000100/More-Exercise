treated_patients = 0
untreated_patients = 0
doctors = 7
number_of_days = int(input())
number_of_patients = 0

for days in range(1, number_of_days + 1):
    number_of_patients = int(input())
    if days % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    else:
        doctors = doctors
    if number_of_patients > 7:
        untreated_patients += number_of_patients - doctors
        treated_patients += doctors
    else:
        treated_patients += number_of_patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")