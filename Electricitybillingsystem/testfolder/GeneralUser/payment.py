import pymysql
import time
from decimal import Decimal
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


def pay_card(meter_number):
    print("payment through card")

    #fetch bill from meter number
    query = "SELECT  Bills.total_amount FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
    mycursor.execute(query,(meter_number))
    bills = mycursor.fetchone()
    if bills:
       totalamount,month = bills
       print(f"bills for month {month} total amount{totalamount}") 

    #card information    
    bill_month = input("billing month: ").strip().lower()
   

    #date and time 
    current_datetime =  datetime.now()
  
    

    getBill_id = f"SELECT  Bills.bill_id FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = {meter_number}"
    mycursor.execute(getBill_id)

    mybills = mycursor.fetchone()
    
    bill_id = mybills[0]

    #query to add the payment to payment table
    check_payment = "SELECT * FROM payments WHERE bill_id = %s AND billing_month = %s"
    mycursor.execute(check_payment,(bill_id,bill_month))
    existing_payment = mycursor.fetchone()

    if existing_payment:
        print(f"payment for this month : {bill_month} exist")
    else:
        cardNumber = input("\ninput card number: ")
        expirydate = input("input EndDate: ")
        CVC = input("input CVC number: ")
        amount = input("amount to pay: ").strip()

        if amount == totalamount:
            bill_Query = "INSERT INTO Payments (bill_id,date_of_payment, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s,%s)"
            mycursor.execute(bill_Query,(bill_id,current_datetime,amount,"CARD",bill_month,"PAYED"))

    
            mydb.commit()
            print("processing payment .........")
            time.sleep(3)
            #query that updates status for bill table
            update_query = "UPDATE Bills SET payment_STATUS = (%s) WHERE billing_month = %s"
            mycursor.execute(update_query,("PAYED",bill_month))
            mydb.commit()
            time.sleep(3)
            print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payement succesfull")
            generate_reciept(meter_number)
        elif amount < totalamount:
            bill_Query = "INSERT INTO Payments (bill_id,date_of_payment, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s,%s)"
            mycursor.execute(bill_Query,(bill_id,current_datetime,amount,"CARD",bill_month,"PAYED"))

    
            mydb.commit()
            print("processing payment .........")
            time.sleep(3)
            #query that updates status for bill table
            update_query = "UPDATE Bills SET payment_STATUS = (%s) WHERE billing_month = %s"
            mycursor.execute(update_query,("PARTIAL PAYMENT",bill_month))
            mydb.commit()
            time.sleep(3)
            print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payement succesfull")
            generate_reciept(meter_number)    

        elif amount > totalamount:
            bill_Query = "INSERT INTO Payments (bill_id,date_of_payment, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s,%s)"
            mycursor.execute(bill_Query,(bill_id,current_datetime,amount,"CARD",bill_month,"PAYED"))

    
            
            print("processing payment .........")
            time.sleep(3)
            #query that updates status for bill table
            update_query = "UPDATE Bills SET payment_STATUS = (%s) WHERE billing_month = %s"
            mycursor.execute(update_query,("PAYED",bill_month))
            mydb.commit()
            time.sleep(3)
            print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payement succesfull")
            generate_reciept(meter_number)




#payment with transfer
def pay_transfer(meter_number = "hel225967"):
    print("payment with transfer")
    #fetch bill from meter number
   
   
    query = "SELECT  Bills.total_amount ,Bills.billing_month  FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s AND Bills.payment_STATUS = 'unpaid' "
    mycursor.execute(query,(meter_number))
    bills = mycursor.fetchone()

    if bills:
        totalamonut,month = bills
        print(f"bills for month {month} total amount{totalamonut}")


        bill_month = input("billing month: ").strip().lower()
        
        

        #date and time 
        current_datetime =  datetime.now()
    
        getBill_id = "SELECT  Bills.bill_id FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
        mycursor.execute(getBill_id,(meter_number))

        mybills = mycursor.fetchone()
        
        bill_id = mybills[0]

        check_payment = "SELECT * FROM payments WHERE bill_id = %s AND  billing_month = %s"
        mycursor.execute(check_payment,(bill_id,bill_month))
        existing_payment =  mycursor.fetchone()

        if existing_payment:
            print(f"payment for this Month : {bill_month} exists")
        else:
            print(f"\nmake a tranfer of ₦{totalamonut} to the account below")
            print("\nAccount name : Excel power distribution company (E-PDC)")
            print("Account number --------------- 00124875963")
            print("Bank ------------------------- United Bank of Africa 🏦")
            amount = Decimal(input("Enter amount to pay: ").strip())
            #query to add the payment to payment table
            if amount == totalamonut:
                bill_Query = "INSERT INTO Payments (bill_id,date_of_payment, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s,%s) "
                mycursor.execute(bill_Query,(bill_id,current_datetime,amount,"TRANSFER",bill_month,"PAID"))
                mydb.commit()
                print("processing payment .........")

                update_query = "UPDATE Bills SET payment_STATUS = (%s) WHERE billing_month = %s"
                mycursor.execute(update_query,("PAID",month))

                mydb.commit()
                time.sleep(3)
                print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payement succesfull")
                generate_reciept(meter_number) 
            elif amount < totalamonut:
                bill_Query = "INSERT INTO Payments (bill_id,date_of_payment, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s,%s) "
                mycursor.execute(bill_Query,(bill_id,current_datetime,amount,"TRANSFER",bill_month,"PARTIAL PAYMENT"))
                mydb.commit()
                print("processing payment .........")

                update_query = "UPDATE Bills SET payment_STATUS = (%s) WHERE billing_month = %s"
                mycursor.execute(update_query,("PARTIAL PAYMENT",month))
                mydb.commit()
                time.sleep(3)
                print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payement succesfull")
                generate_reciept(meter_number)

            elif amount > totalamonut:
                bill_Query = "INSERT INTO Payments (bill_id,date_of_payment, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s,%s) "
                mycursor.execute(bill_Query,(bill_id,current_datetime,amount,"TRANSFER",bill_month,"PAID"))
                mydb.commit()
                print("processing payment .........")
                update_query = "UPDATE Bills SET payment_STATUS = (%s) WHERE billing_month = %s"
                mycursor.execute(update_query,("PAID",month))
                mydb.commit()
                time.sleep(3)
                print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payement succesfull")
                generate_reciept(meter_number)
            else:
                print(",,,,,,,,,,,,,,,")
                
                           
    else:
        print("no unpaid bills")

   


#generate reciept function
def generate_reciept(meter_number ):
    query = '''SELECT Customer.fullName, Customer.meter_number, Customer.address,
           Bills.billing_month, Bills.units_used, Bills.total_amount,
           Payments.billing_month, Payments.date_of_payment, Payments.amount_paid,
           Payments.Payment_STATUS, Payments.payment_id
           FROM Customer 
           INNER JOIN Bills ON Customer.customer_id = Bills.customer_id 
           INNER JOIN Payments ON Bills.bill_id = Payments.bill_id 
           WHERE Customer.meter_number = %s 
           ORDER BY Payments.date_of_payment DESC LIMIT 1'''

    mycursor.execute(query,meter_number)
    customer = mycursor.fetchone()

    
    print("\n\n\t\t\tExcel Power Distribution Company (E-PDC) RECEIPT")
    print("=================================================================================")
    print("Your payment was successful ✅")
    print("---------------------------------------------------------------------------------")
    print("Transaction Details:\n")
    print(f"Customer Name:      {customer[0]}")
    print(f"Meter Number:       {customer[1]}")
    print(f"Address:            {customer[2]}")
    print(f"Billing Month:      {customer[6]}")
    print(f"Units Used:         {customer[4]}")
    print(f"Total Bill:         ₦{customer[5]}")
    print(f"Amount Paid:        ₦{customer[8]}")
    print(f"VAT:                7.5%")
    print(f"Payment ID:         {customer[10]}")
    print(f"Payment Status:     {customer[9]}")
    print(f"Date of Payment:    {customer[7]}")
    print("---------------------------------------------------------------------------------")
    print("\n\t\tTHANK YOU FOR USING E-Electricity 💡")
    





   


#payment menu
def payment_menu(meter_number):
    print("Select a payment method")
    print("\n") 
    print("1.Pay with card 💳 ")
    print("2.pay with transfer ")
    print("3.EXIT ")

    selection = input("select an option: ").strip()
    if selection == "1":
        pay_card(meter_number)
    elif selection == "2":
        pay_transfer(meter_number)
    elif selection == "3":
        return
    else:
        print("invalid")
    

def my_reciept():
    pass







def payment(meter_number):
    print("1.pay bills")
    print("2.Generate Reciept")
    print("3.Exit")

    option = input("select an option: ").strip()

    if option == "1":
        payment_menu(meter_number)
    elif option == "2":
        pass
    elif option == "3":
        return
    else:
        print("invalid")

