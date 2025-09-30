#class task 5
class Student:
    def __init__(self,name,age,cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display_info(self):
        print(f"student name {self.name} , Age is {self.age}, current cgpa is {self.cgpa}")

Std = Student("Ade","15","4.6")
std1 = Student("JOHN BULL","19","4.9")

Std.display_info()
std1.display_info()

#class task 6
class BankAccount:
    def __init__(self,account_number,balance,account_name):
        self.account_number = account_number
        self.balance = balance
        self.account_name = account_name

    def deposit(self,amount):
        self.balance += amount
        print(f"you made a deposit of {amount} and balance is {self.balance}")
    
    def withdraw(self,amount):
        self.balance -= amount
        print(f"you made a withdraw of {amount} and balance is {self.balance}")

    def check_balance(self):
        print(f"your balance is {self.balance}")

user1 = BankAccount("1024556",0,"TOBI")
user1.deposit(500)
user1.withdraw(200)
user1.check_balance()