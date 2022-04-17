season = input()
type_of_group = input()
num_student = int(input())
num_nights = int(input())
sum_night = 0
sport = ""

if season == "Spring" and (type_of_group == "boys" or type_of_group == "girls" or type_of_group == "mixed"):

    if type_of_group == "boys":
        sum_night = (num_student * 7.2) * num_nights
        sport = "Tennis"
    elif type_of_group == "girls":
        sum_night = (num_student * 7.2) * num_nights
        sport = "Athletics"
    elif type_of_group == "mixed":
        sum_night = (num_student * 9.5) * num_nights
        sport = "Cycling"

elif season == "Winter" and (type_of_group == "boys" or type_of_group == "girls" or type_of_group == "mixed"):

    if type_of_group == "boys":
        sport = "Judo"
        sum_night = (num_student * 9.6) * num_nights
    elif type_of_group == "girls":
        sport = "Gymnastics"
        sum_night = (num_student * 9.6) * num_nights
    elif type_of_group == "mixed":
        sum_night = (num_student * 10) * num_nights
        sport = "Ski"

else:

    if type_of_group == "boys":
        sum_night = (num_student * 15) * num_nights
        sport = "Football"
    elif type_of_group == "girls":
        sum_night = (num_student * 15) * num_nights
        sport = "Volleyball"
    elif type_of_group == "mixed":
        sum_night = (num_student * 20) * num_nights
        sport = "Swimming"

if num_student < 10:
    print(f"{sport} {sum_night:.02f} lv.")
elif num_student < 20:
    print(f"{sport} {sum_night * 0.95:.02f} lv.")

elif num_student < 50:
    print(f"{sport} {sum_night * 0.85:.02f} lv.")
else:
    print(f"{sport} {sum_night * 0.50:.02f} lv.")