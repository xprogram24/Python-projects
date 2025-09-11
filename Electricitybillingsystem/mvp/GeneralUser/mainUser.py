import pymysql
from accountInfo import accountInfo
from Billing_info import billing_info
from payment import payment
mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="customer",
    password = "mycustomer",
    database="electricBilling_DB"
)

mycursor = mydb.cursor()
print("connection successful")




def menu():
    while True:
        print("\n==================== welcome to E-electricity User Menu ===========================")
        print("please select an option")
        print("\n1.Account Dashboard")
        print("2.Billing info")
        print("3.payment ")
        print("4.Get Reciept")
        print("5.Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            accountInfo()
        elif choice == '2': 
            billing_info()
        elif choice == '3':
            payment()
        elif choice == '4':
            pass
        elif choice == '5':
            print("goodbye")
            break
        else :
            print("invalid option")
