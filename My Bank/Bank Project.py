import sqlite3 as db

print()
print("*" * 50)
print("Welcome to my private bank!")
print("*" * 50)

connect = db.connect("data.db")
cursor = connect.cursor()
sql = 'CREATE TABLE USERS("name" TEXT, "email" VARCHAR(30) UNIQUE, "mobile" INTEGER UNIQUE, "password" TEXT, "amount" INTEGER);'
try:
    cursor.execute(sql)
except db.OperationalError:
    pass


class Customer:
    """This is for existing customers"""

    def __init__(self, name, email, mobile, amount):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.amount = amount

    def zone(self):
        print()
        print("*" * 50)
        print("\nHi", self.name + "!", "Welcome to Private Bank")
        print("Available features:\n1. Deposit\n2. Withdraw\n3. My Balance\n4. My Info\n5. Logout")
        option = input("Enter your choise: ")
        if option == "1":
            Customer.deposit(self)
        elif option == "2":
            Customer.withdraw(self)
        elif option == "3":
            print("\nYour Account Balance is:", self.amount)
            self.zone()
        elif option == "4":
            Customer.info(self)
        elif option == "5":
            print("Logging out!")
        else:
            print("Invalid selection! please try again...")
            self.zone()

    def balance(self):
        query = "SELECT * FROM USERS WHERE email = '%s'" % self.email
        cursor.execute(query)
        user_data = cursor.fetchone()
        if user_data is not None:
            amount = user_data[4]
            return amount

    def info(self):
        print("\nYour Account Info")
        print("Your Name        :", self.name)
        print("Your Email ID    :", self.email)
        print("Mobile Number    :", self.mobile)
        print("Account Balance  :", self.amount)
        Customer.zone(self)

    def deposit(self):
        global amount
        try:
            amount = abs(int(input("\nEnter the amount to deposit: ")))
        except:
            print("Invalid input")
            self.deposit()
        email = self.email
        query = "SELECT * FROM USERS WHERE email = '%s'" % email
        cursor.execute(query)
        user_data = cursor.fetchone()
        self.amount = user_data[4] + amount
        query = "UPDATE USERS SET amount = %i WHERE email = '%s'" % (self.amount, email)
        cursor.execute(query)
        connect.commit()
        print("Transaction completed successfully!")
        print("Now your account balance is topped up from %i to %i" % (user_data[4], self.amount))
        Customer.zone(self)

    def withdraw(self):
        global amount
        try:
            amount = abs(int(input("\nEnter the amount to withdraw: ")))
        except:
            print("Invalid input")
            self.deposit()
        query = "SELECT * FROM USERS WHERE email = '%s'" % self.email
        cursor.execute(query)
        user_data = cursor.fetchone()

        if user_data[4] > amount:
            self.amount = user_data[4] - amount
            query = "UPDATE USERS SET amount = %i WHERE email = '%s'" % (self.amount, self.email)
            cursor.execute(query)
            connect.commit()
            print("Transaction completed successfully!")
            print("Now your account balance is drained from %i to %i" % (user_data[4], self.amount))
            Customer.zone(self)
        else:
            print("Transaction failed due to insufficient account balance!")
            Customer.zone(self)


class Bank:
    """This class is used for Login purpose"""

    @staticmethod
    def register():
        try:
            print("\nCreating a new account")
            name = input("Enter your name: ")
            email = input("Enter your email address: ")
            mobile = int(input("Enter your mobile number: "))
            password = input("Enter your password: ")
            amount = int(input("Enter the amount to deposit: "))
            query = "INSERT INTO USERS (name, email, mobile, password, amount) VALUES ('%s', '%s', %i, '%s', %i)" % (
                name, email, mobile, password, amount)
            cursor.execute(query)
            connect.commit()
            print("Hi", name + "! Your Account is Registered Successfully!")
            Bank.login()
        except:
            print("Invalid inputs! please try again...")
            Bank.register()

    @staticmethod
    def login():
        print("\nLogin to your account")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        query = "SELECT * FROM USERS WHERE email = '%s'" % email
        cursor.execute(query)
        user_data = cursor.fetchone()
        if user_data is not None:
            if email == user_data[1]:
                if password == user_data[3]:
                    name = user_data[0]
                    mobile = user_data[2]
                    amount = user_data[4]
                    user = Customer(name, email, mobile, amount)
                    user.zone()
                else:
                    print("Invalid Password!")
                    Bank.login()
            else:
                print("Invalid email!")
                Bank.login()
        else:
            print("Invalid email!")
            Bank.login()


# Entering inside of Bank
print("\nChoose correct option!\n1. I'm an Existing Customer\n2. I'm a New Customer\n3. Show Customers")
while True:
    choise = input("\nEnter your choise: ")
    if choise == "1":
        Bank.login()
        break
    elif choise == "2":
        Bank.register()
        break
    elif choise == "3":
        cursor.execute("SELECT * FROM USERS")
        users = cursor.fetchall()
        serial = 1
        if len(users) != 0:
            for user in users:
                print(str(serial) + ":", user[0], "(email: %s)" % user[1])
                serial += 1
        else:
            print("No customers to show!")
        break
    else:
        print("Invalid selection! please try again...")
