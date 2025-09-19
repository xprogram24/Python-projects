'''from datetime import datetime

current_datetime =  datetime.now()
print(current_datetime)
day = current_datetime.date()'''

#fetch bill from meter number
import pymysql
import time
from datetime import datetime
from tabulate import tabulate
from decimal import Decimal
mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="admin",
    password = "myadmin",
    database="electricBilling_DB"
)

mycursor = mydb.cursor()

'''def generate_reciept():
    print("\t\t\t\t\t\t\tExcel power distribution company (E-PDC) RECIEPT")
    print("\nYour payment was successful")
    print("--------------------------------------------------------------------------------------------------")
    print("\nYour transaction details as follows")
    print("Meter number: hel147896")
    print("--------------------------------------------------------------------------------------------------")
    print("\nCustomer Name                                        ADEBAYO PAUL")
    print("\nAddress                                              11 BOLA AHMED STREET, IKEJA")  
    print("\nService Name:                                        Excel power distribution company (E-PDC")
    print("\nMeter Number                                         hel147896")
    print("\nAmount                                               #35,000")
    print("\nVAT                                                  7.5%")
    print("\nTotal amount Paid                                    #35,200")
    print("\npayment ID                                           15")
    print("\nStatus                                               PAID")
    print(f"\nDate                                                {day}")
    print("--------------------------------------------------------------------------------------------------")
    print("\n                               THANK YOU FOR USING E-Electricity")
#generate_reciept()'''



'''query = SELECT Customer.fullName, Customer.meter_number, Customer.address,
           Bills.billing_month,Bills.units_used,Bills.total_amount,Payments.billing_month,
           Payments.date_of_payment,Payments.amount_paid,Payments.Payment_STATUS FROM Customer 
           INNER JOIN Bills ON Customer.customer_id = Bills.customer_id INNER JOIN Payments ON 
           Bills.bill_id = Payments.bill_id WHERE meter_number = %s 

meter_number = input("enter meter number")

mycursor.execute(query,(meter_number))
print("yooo")

customer = mycursor.fetchall()
for customers in customer:
    print("\t\t\t\t\t\t\tExcel power distribution company (E-PDC) RECIEPT")
    print("\nYour payment was successful")
    print("--------------------------------------------------------------------------------------------------")
    print("\nYour transaction details as follows")
    print(f"Meter number: {customers[1]}")
    print("--------------------------------------------------------------------------------------------------")
    print(f"\nCustomer Name                                        {customers[0]}")
    print(f"\nAddress                                              {customers[2]}")  
    print("\nService Name:                                        Excel power distribution company (E-PDC")
    print(f"\nMeter Number                                          {customers[1]}")
    print("\nVAT                                                  7.5%")
    print(f"payment month                                           {customers[6]}")
    print(F"units used                                              {customers[4]}")
    print(f"\nTotal amount Paid                                     {customers[5]}")
    print("\npayment ID                                           15")
    print(f"\nStatus                                               {customers[9]}")
    print(f"\nDate                                                {customers[7]}")
    print("--------------------------------------------------------------------------------------------------")
    print("\n                               THANK YOU FOR USING E-Electricity")'''




#tracking paid and unpaid pils
'''def tracking():
    print("1.track paid")
    print("2.unpaid")
    print("3.exit")

    selection = input("click option: ")
    if selection == "1":
        
        view_Query = SELECT Customer.fullName, Customer.meter_number, 
                        Bills.billing_month,Bills.units_used,Bills.total_amount,
                        Bills.payment_STATUS
                        FROM Customer INNER JOIN Bills ON 
                        Customer.customer_id = Bills.customer_id 
                         WHERE Bills.payment_STATUS = "PAYED" 
        mycursor.execute(view_Query)
        customers = mycursor.fetchall()
        header = ["Full Name","Meter number","Billing Month","units_used","Total Amount (#)","Date","Payment_STATUS"]
        print(tabulate(customers,headers=header, tablefmt="fancy_grid"))
      
  
    elif selection == "2":
        view_Query = SELECT Customer.fullName, Customer.meter_number, 
                        Bills.billing_month,Bills.units_used,Bills.total_amount,
                        Bills.payment_STATUS
                        FROM Customer INNER JOIN Bills ON 
                        Customer.customer_id = Bills.customer_id 
                         WHERE Bills.payment_STATUS = "unpaid" 
        mycursor.execute(view_Query)
        customers = mycursor.fetchall()
        header = ["Full Name","Meter number","Billing Month","units_used","Total Amount (#)","Date","Payment_STATUS"]
        print(tabulate(customers,headers=header, tablefmt="fancy_grid"))
    elif selection == "3":
        return
    else:
        print("invalid")


tracking()
'''

#figure out if user has paid
'''def pay_transfer(meter_number = "hel225967"):
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
            else:
                print(",,,,,,,,,,,,,,,")
                
                           
    else:
        print("no unpaid bills")

pay_transfer()


def pay_card(meter_number):
    print("payment through card")

    #fetch bill from meter number
    query = "SELECT  Bills.total_amount FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
    mycursor.execute(query,(meter_number))
    bills = mycursor.fetchone()
  

    #card information    
    bill_month = input("billing month: ").strip()
    cardNumber = input("\ninput card number: ")
    expirydate = input("input EndDate: ")
    CVC = input("input CVC number: ")
    amount = input("amount to pay: ").strip()

    #date and time 
    current_datetime =  datetime.now()
  
    

    getBill_id = f"SELECT  Bills.bill_id FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = {meter_number}"
    mycursor.execute(getBill_id)

    mybills = mycursor.fetchone()
    
    bill_id = mybills[0]

    #query to add the payment to payment table
    bill_Query = "INSERT INTO Payments (bill_id,date_of_payment, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(bill_Query,(bill_id,current_datetime,amount,"CARD",bill_month,"PAYED"))

    
    mydb.commit()
    print("processing payment .........")
    time.sleep(3)
    #query that updates status for bill table
    update_query = "UPDATE Bills SET payment_STATUS = (%s)"
    mycursor.execute(update_query,("PAYED"))
    mydb.commit()
    time.sleep(3)
    print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payement succesfull")
    
'''

def update_bill():
    meter_number = input("enter a meter number: ").strip()
  

    searchQuery = "SELECT Customer.customer_id, Customer.fullName, Customer.meter_number, Bills.bill_id, Bills.billing_month, Bills.units_used, Bills.rate_per_unit, Bills.total_amount,Bills.Payment_STATUS FROM Bills INNER JOIN  Customer ON Bills.customer_id = Customer.customer_id WHERE Customer.meter_number = %s AND Bills.Payment_STATUS = %s"
    mycursor.execute(searchQuery,(meter_number,"unpaid"))
    customers = mycursor.fetchall()
    header = ["Customer_id","Full Name","Meter number", "Bill ID","Billing Month","units_used","Rate","Total Amount (#)","Payment_STATUS"]
    print(tabulate(customers,headers=header, tablefmt="fancy_grid"))
    
    if not customers:
        print(" no unpaid bills found")
    else:
        print("update unit used and billing month")
        newUnit = float(input("input unit used: "))
        newMonth = input("type  month : ")
        rate = 66.00
    
        bill = newUnit * rate 
        VAT = 0.075 * bill
        total_amount = bill + VAT
        #get billl id
        MYbill_id = customers[0][3]
        update = "UPDATE  Bills SET Billing_month = %s , units_used = %s,total_amount = %s WHERE bill_id = %s"
        mycursor.execute(update,(newMonth,newUnit,total_amount, MYbill_id,))
        mydb.commit()

        print("change sucessful")
        searchQuery = "SELECT Customer.customer_id, Customer.fullName, Customer.meter_number, Bills.bill_id, Bills.billing_month, Bills.units_used, Bills.rate_per_unit, Bills.total_amount,Bills.Payment_STATUS FROM Bills INNER JOIN  Customer ON Bills.customer_id = Customer.customer_id WHERE Customer.meter_number = %s AND Bills.Payment_STATUS = %s"
        mycursor.execute(searchQuery,(meter_number,"unpaid"))
        customers = mycursor.fetchall()
        header = ["Customer_id","Full Name","Meter number", "Bill ID","Billing Month","units_used","Rate","Total Amount (#)","Payment_STATUS"]
        print(tabulate(customers,headers=header, tablefmt="fancy_grid"))

   
update_bill()













'''def myMeternumber():
   global x 
   x = 15
   return x

def result():
    myMeternumber()
    print(x)

#filling admin page with data
import pymysql
mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="admin",
    password = "myadmin",
    database="electricBilling_DB"
)

mycursor = mydb.cursor()
print("connection successful")

query = "INSERT INTO myAdmin (adminName,email) VALUE(%s,%s)"
values = [("Williams","willy11@yahoo.com"),
          ("Johnson","jony5k@gmail.com"),
          ("Excel","cexcel@gmail.com")
          ]
mycursor.executemany(query,values)
mydb.commit()
print("done")'''


