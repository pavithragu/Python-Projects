import datetime


def age_calculator():
    try:
        print("\n<------------------- Age Calculator ------------------->\n")
        print("Example: 15-06-1997")
        dob = (datetime.datetime.strptime(input("Enter Your DOB: "), "%d-%m-%Y").date())
        days = (datetime.date.today() - dob).days

        print("Your age in years:", int(days // 365.25), "years and", int(days % 365.25), "days")
        print("Your age in months:", int(days / (365.25 / 12)), "months")
        print("Your age in weeks:", int(days / 7), "weeks")
        print("Your age in days:", days, "days")
        print("Your age in hours:", days * 24, "hours")
        print("Your age in minutes:", days * 24 * 60, "minutes")

    except:
        print("Invalid Date of Birth! Please try again...")
        age_calculator()

    else:
        choise = input("\nPress 1 to continue...")
        if choise == "1":
            age_calculator()
        else:
            print("\nThank you so much for using Age Calculator...")


age_calculator()
