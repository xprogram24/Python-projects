import pymysql

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="customer",
    password = "mycustomer",
    database="electricBilling_DB"
)

mycursor = mydb.cursor()
print("connection successful")

def account_info():
    pass


def menu():
    while True:
        print("==================== welcome to E-electricity User Menu ===========================")
        print("please select an option")
        print("\n1.Account Dashboard")
        print("2.Billing info")
        print("3.payment ")
        print("4.Download Reciept")
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
menu()