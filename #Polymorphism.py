#Polymorphism


#Parent Class User
class User:
    name = "Mark"
    email = "mark@example.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: \n>>>")
        entry_email = input("Enter your email: \n>>>")
        entry_password = input("Please enter PW: \n>>>")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome Back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect")

#Child class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

    #Polymorphism here will take place in replacing password for pin
    def getLoginInfo(self):
        entry_name = input("Enter your name: \n>>>")
        entry_email = input("Enter your email: \n>>>")
        entry_pin = input("Please enter PIN: \n>>>")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome Back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")

customer = User()
customer.getLoginInfo()
Manager = Employee()
Manager.getLoginInfo()




















