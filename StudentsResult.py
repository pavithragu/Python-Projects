class Result:
    """This class is used to check the result of the students"""

    def __init__(self, regno, name, standard, section, mark, result):
        self.regno = regno
        self.name = name
        self.standard = standard
        self.section = section
        self.mark = mark
        self.result = result

    def student(self):
        print('RegisterNo :', self.regno)
        print('Name :', self.name)
        print('Class :', self.standard)
        print('Section :', self.section)
        print('Mark :', self.mark)
        print('Result :', self.result)


Raju = Result(622614114001, 'Raju', '10th Std', 'A-Section', '400', 'Pass')
Ragu = Result(622614114002, 'Ragu', '10th Std', 'B-Section', '150', 'Fail')
Sathiya = Result(622614114003, 'Sathiya', '10th Std', 'C-Section', '350', 'Pass')
Suvitha = Result(622614114004, 'Suvitha', '10th Std', 'B-Section', '499', 'Pass')
Thirumalai = Result(622614114005, 'Thirumalai', '10th Std', 'A-Section', '412', 'Pass')
Dharnesh = Result(622614114006, 'Dharnesh', '10th Std', 'C-Section', '298', 'Pass')
Maishri = Result(622614114007, 'Maishri', '10th Std', 'A-Section', '488', 'Pass')
Adhi = Result(622614114008, 'Adhi', '10th Std', 'A-Section', '80', 'Fail')
Murugan = Result(622614114009, 'Murugan', '10th Std', 'C-Section', '102', 'Fail')
Thilagavathi = Result(622614114010, 'Thilagavathi', '10th Std', 'C-Section', '170', 'Fail')


def start():
    try:
        print("\n<------------------- Student Result ------------------->\n")
        a = input("Enter the student name to view the result: ")
        a = a.title()
        a = globals()[a]
        a.student()

    except KeyError:
        print("The Entered Name is Not Available! Please Type correct Name Below...")
        start()

    except:
        print("Something Went Wrong! Please Try Again...")
        start()

    else:
        choice = input("\nEnter 1 to continue or any other to exit: ")
        if choice == "1":
            start()
        else:
            print("\nThank you so much for using Student Result!")


start()
