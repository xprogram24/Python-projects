import pymysql
import time
from tabulate import tabulate
mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="customer",
    password = "mycustomer",
    database="electricBilling_DB"
)
 
mycursor = mydb.cursor()
print("connection successful")


def accountInfo(meter_number):
    print("your account info")
    viewQuery = "SELECT customer_id,meter_number,fullName,address,phoneNumber,email FROM Customer WHERE meter_number =%s"
    mycursor.execute(viewQuery,(meter_number))
    user = mycursor.fetchall()
    time.sleep(1)
    headers = ["ID","Meter_number","Full name","Home Address","Phone Number","Email"]
    print(tabulate(user,headers=headers,tablefmt="fancy_grid"))





