#main py file for electricty billing system

import pymysql
from customer import addCustomer,viewCustomer , updateCustomer
from bill import generate_bill,view_bills,update_bill
from payment import view_payment,generatepdf,tracking
from reportAnalysis import Totalrevenue,outstanding_balance,monthly_usage
import time
try:
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


    #function to display customer menu
    def customer_menu():

        while True:
            print("\n======customer management======")
            print("1.Add new customers")
            print("2.update a customers information")
            print("3.view all customers")
            print("4 exit customer managment")

            option = input("\nselect an option: ")
            if option == "1":
                addCustomer()
            elif option == "2":
                updateCustomer()
            elif option == "3":
                viewCustomer()
            elif option == '4':
                print("thank you for using customer managment")
                break
            else:
                print("invalid")

    #function to display bill menu
    def bill_menu():
        

        while True:

            print("\n======Billing management======")
            print("1.Generate bills for each customer")
            print("2.update bills if mistakes happen")
            print("3.view all bills")
            print("4 exit billing managment")

            option = input("\nselect an option: ")
            if option == "1":
                print("generate bills ")
                generate_bill()
            elif option == "2":
                update_bill()
            elif option == "3":
                
                view_bills()
            elif option == '4':
                print("thank you for using bill managment")
                break
            else:
                print("invalid")



    #function to display payment menu
    def payment_managment():
        
        while True:

            print("\n======payment management======")
            print("1.view payment ")
            print("2.Tracking pending/unpaid bills")#optional
            print("3.Generate reciepts(PDF)")
            print("4 exit payment managment")

            option = input("\nselect an option: ")
            if option == "1":
                print("payment record")
                view_payment()
            elif option == "2":
                tracking()
            elif option == "3":
                generatepdf()
            elif option == '4':
                print("thank you for using payment managment")
                break
            else:
                print("invalid")

    #function to display report analysis menu
    def analysis():

        while True:
            time.sleep(1)
            print("\n======Report & Analytics======")
            print("1.Total revenue collected")
            print("2.outstanding balance")
            print("3.monthly usage trend")
            print("4 exit Report & analytics")

            option = input("\nselect an option: ")
            if option == "1":
                Totalrevenue()
            elif option == "2":
                outstanding_balance()
            elif option == "3":
                monthly_usage()
            elif option == '4':
                print("thank you for report & analytics")
                break
            else:
                print("invalid")

    # main menu option
    def menu():
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
                bill_menu()
            elif choice == '3':
                payment_managment()
            elif choice == '4':
                analysis()
            elif choice == '5':
                print("goodbye")
                break
            else :
                print("invalid option")
except Exception as e:
    print("database connection failed",e)