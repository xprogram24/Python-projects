'''from datetime import datetime

current_datetime =  datetime.now()
print(current_datetime)
day = current_datetime.date()'''

#fetch bill from meter number
import pymysql
from tabulate import tabulate
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


