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

#create menu option

while True:
    print("=====================welcome to E-electricity Admin option===========================")
    print("\n please select an option")
    print("1.Customer managment")
    print("2.Billing managment")
    print("3.payment Managment")
    print("4.report analysis")
    print("5.Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        pass
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