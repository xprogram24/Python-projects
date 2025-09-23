import pymysql
from tabulate import tabulate
import time
mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="customer",
    password = "mycustomer",
    database="electricBilling_DB"
)

mycursor = mydb.cursor()
print("connection successful")
 
def billing_info(meter_number):
    print("your billing info")
    bill_Query = "SELECT Bills.bill_id, Customer.customer_id, Customer.meter_number , Customer.fullName, Bills.billing_month, Bills.units_used, Bills.total_amount,Bills.payment_STATUS FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
    mycursor.execute(bill_Query,(meter_number))
    user = mycursor.fetchall()
    time.sleep(1)
    headers = ["Bills ID","Customer ID","Meter Number","Name","Bill Month","Unit used","Total bills (₦)","Status"]
    print(tabulate(user,headers=headers,tablefmt="fancy_grid"))
