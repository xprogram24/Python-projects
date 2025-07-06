class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def prop1(self):
        print(f"my name is {self.name} and i am {self.age}")

st1 = Student('excel','15')
st1.prop1()

"""
A Car class with:

Attributes: brand, year

Method: start_engine() that prints "{brand} engine started" """

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    
    def start_engine(self):
        print(f"{self.brand} engine started")
    
newCar = Car('ford','2016')
newCar.start_engine()

"""
Task:
Create a class Book with:

Attributes: title and author

Method: display_info() that prints:
"Title: [title], Author: [author]" """

'''Add a method is_written_by(name) to your Book class:

It should return True if name matches the book’s author.'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Tittle: {self.title}c, Author: {self.author}")

    def is_written_by(self):
        print(f"written by {self.author}")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")

book1.display_info()
book1.is_written_by()

if book1.author == "F. Scott Fitzgerald":
    print("True")
else:
    print("False")


"""
Create a class Student:

Attributes: name and score

Method: update_score(new_score) — updates the score.

Method: display() — prints: "Name: [name], Score: [score]" """

class Student:
    def __init__(self,name, score):
        self.name = name
        self.score = score
    
    def update_score(self,new_Score ):
        print(f"old score : {self.score} ")

        self.new_score = new_Score
        print(f"old score : {self.score} , new score : {self.new_score}")

    def display(self):
        print(f"Name : {self.name} , Score: {self.score}")

s1 = Student('excel ', '50')
s1.update_score(10)
s1.display()

'''
Write a BankAccount class:

Attributes: owner and balance

Method: deposit(amount) — adds to balance.

Method: withdraw(amount) — subtracts from balance if enough funds, else print "Insufficient funds".

Method: display_balance() — prints "Balance: $[balance]".'''

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        print(f'balance = {self.balance}')

        self.balance += amount

        print(f'deposit : {amount} new balance is :{self.balance}')

    def withdraw(self,amount):
        print(f"balance {self.balance}")
        
        self.balance -= amount

        print(f'withdrew : {amount} new balance is :{self.balance}')

    def ybalance(self):
       
        print(f'balance is : {self.balance}')

tobs = BankAccount('tobi',200)   
tobs.deposit(10)
tobs.withdraw(20)
tobs.ybalance()