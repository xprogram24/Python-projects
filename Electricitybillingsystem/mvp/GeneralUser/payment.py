import pymysql
import time
#from tabulate import tabulate
from datetime import datetime

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="customer",
    password = "mycustomer",
    database="electricBilling_DB"
)

mycursor = mydb.cursor()
print("connection successful")


def pay_card():
    print("payment through card")

    #fetch bill from meter number
    meter_number = input("input meter number: ").strip()
    query = "SELECT  Bills.total_amount FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
    mycursor.execute(query,(meter_number))
    bills = mycursor.fetchall()
    for bill in bills:
        print(f"your bill is ₦{bill[0]}")

    #card information    
    bill_month = input("billing month: ").strip()
    cardNumber = input("\ninput card number: ")
    expirydate = input("input EndDate: ")
    CVC = input("input CVC number: ")
    amount = input("amount to pay: ").strip()

    #date and time 
    current_datetime =  datetime.now()
  
    

    getBill_id = "SELECT  Bills.bill_id FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
    mycursor.execute(getBill_id,(meter_number))

    mybills = mycursor.fetchone()
    
    bill_id = mybills[0]

    #query to add the payment to payment table
    bill_Query = "INSERT INTO Payments (bill_id,date_of_payment, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(bill_Query,(bill_id,current_datetime,amount,"CARD",bill_month,"PAYED"))
    mydb.commit()
    print("processing payment .........")
    time.sleep(3)
    print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payement succesfull")


#payment with transfer
def pay_transfer():
    print("payment with transfer")
    #fetch bill from meter number
    meter_number = input("input meter number: ").strip()
    bill_month = input("billing month: ").strip()
    query = "SELECT  Bills.total_amount FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
    mycursor.execute(query,(meter_number))
    bills = mycursor.fetchall()
    for bill in bills:
        print(f"your bill is ₦{bill[0]}")

    print(f"\nmake a tranfer of ₦{bill[0]} to the account below")
    print("\nAccount name : Excel power distribution company (E-PDC)")
    print("Account number --------------- 00124875963")
    print("Bank ------------------------- United Bank of Africa 🏦")
    amount = input("amount to payed: ")

    #date and time 
    current_datetime =  datetime.now()
  
    getBill_id = "SELECT  Bills.bill_id FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
    mycursor.execute(getBill_id,(meter_number))

    mybills = mycursor.fetchone()
    
    bill_id = mybills[0]

    #query to add the payment to payment table
    bill_Query = "INSERT INTO Payments (bill_id,date_of_payment, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(bill_Query,(bill_id,current_datetime,amount,"TRANSFER",bill_month,"PAYED"))
    mydb.commit()
    print("processing payment .........")
    time.sleep(3)
    print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payement succesfull")
    
   


#payment menu
def payment_menu():
    print("Select a payment method")
    print("\n") 
    print("1.Pay with card 💳 ")
    print("2.pay with transfer ")
    print("3.EXIT ")

    selection = input("select an option: ").strip()
    if selection == "1":
        pay_card()
    elif selection == "2":
        pay_transfer()
    elif selection == "3":
        return
    else:
        print("invalid")
    

def my_reciept():
    pass







def payment():
    print("1.pay bills")
    print("2.Generate Reciept")
    print("3.Exit")

    option = input("select an option: ").strip()

    if option == "1":
        payment_menu()
    elif option == "2":
        pass
    elif option == "3":
        return
    else:
        print("invalid")

