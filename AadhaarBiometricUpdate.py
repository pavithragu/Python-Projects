import datetime


def initialize():
    now = datetime.date.today()
    print("\n<------------------- Aadhaar Biometric ------------------->\n")

    try:
        print("Example: 15/06/1997")
        dob = datetime.datetime.strptime((input('Please Enter Your DOB: ')), '%d/%m/%Y').date()
        days = (now - dob).days
        print("Result:", end=' ')
        if days > 1830:
            print("You Can Enroll/Update Aadhaar With Bio-Metric Data")
        else:
            print("You Can't Enroll/Update Aadhaar With Bio-Metric Data")

    except:
        print("Invalid Date of Birth! Please try again...")
        initialize()

    else:
        choice = input("\nPress 1 to continue or any other to exit...")
        if choice == "1":
            initialize()
        else:
            print("\nThank you so much for using Aadhaar Biometric!")


initialize()
