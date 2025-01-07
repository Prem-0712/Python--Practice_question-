a = int(input("Enter the month number: "))

if a in [1, 3, 5, 7, 8, 10, 12]:
    months_with_31_days = {
        1: "January",
        3: "March",
        5: "May",
        7: "July",
        8: "August",
        10: "October",
        12: "December"
    }

    print(f"{months_with_31_days[a]} has 31 days.")

elif (a == 2):
    print("February has 28 days")

elif a in [4, 6, 9, 11]:

    months_with_30_days = {
        4: "April",
        6: "June",
        9: "September",
        11: "November"
    }

    print(f"{months_with_30_days[a]} has 30 days.")

else:
    print("invalid month number")