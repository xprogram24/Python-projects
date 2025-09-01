#main py file for electricty billing system

import pymysql

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="admin",
    password = "myadmin",
    database="electricBilling_DB"
)

#create cursor
mycursor = mydb.cursor()
print("db connected to successfully")

def customer_menu():
    print("\n======customer management======")
    print("1.Add new customers")
    print("2.update a customers information")
    print("3.view all customers")
    print("4 exit customer managment")

    while True:
        option = input("\nselect an option: ")
        if option == "1":
            print("add customer")
        elif option == "2":
            print("update customer")
        elif option == "3":
            print("view all customers")
        elif option == '4':
            print("thank you for using customer managment")
            break
        else:
            print("invalid")

#create menu option

while True:
    print("=====================welcome to E-electricity Admin option===========================")
    print("please select an option")
    print("\n1.Customer managment")
    print("2.Billing managment")
    print("3.payment Managment")
    print("4.report analysis")
    print("5.Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
            customer_menu()
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        print("goodbye")
        break
    else :
        print("invalid option")