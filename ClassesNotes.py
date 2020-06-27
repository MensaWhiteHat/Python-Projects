class User:
    #define the attributes of the class
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    acct = 0

class Employee(User):
    base_pay = 11:00
    department = 'General'

#second class that inherits from another class
class Customer(User):
    Mailing_list = True

#define the methods of the class
def login(self):
    entry_email = input("Enter your email: ")
    entry_password = input("please enter pw: ")
    if (entry_email == self.email and entry_password == self.password):
        print("Welcome back, {}!".format(self.name))
    else:
        print("Go away")

new_user = User()

def __init__(self, name, password, accout):
    self.name = name
    self.email = email
    self.password = password
    self.account = account
