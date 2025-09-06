import pymysql

from tabulate import tabulate
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

def generate_bill():
    print("welcome to bill generating")
    meter_number = input("please input meter number :")
    query = "SELECT customer_id FROM Customer WHERE meter_number = %s"
    mycursor.execute(query,meter_number)

    customers = mycursor.fetchone()
    
    customer_id = customers[0]

    billing_month = input("input billing month: ")
    unit = int(input("input unit consumed: "))
    rate = 66.00
    
    bill = unit * rate 
    VAT = 0.075 * bill
    total_amount = bill + VAT
    print(f"bill is {bill}")
    print(f"total bill + vat is {total_amount}")
    bill_query = "INSERT INTO Bills (customer_id, units_used, rate_per_unit, total_amount, billing_month) VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(bill_query,(customer_id,unit,rate,total_amount,billing_month))
    mydb.commit()
    print(f"✅ Bill generated for {meter_number} | Amount: ₦{total_amount} ")

   
generate_bill()

def view_bills():
    Meter_Nnumber = input("input meter Number: ")
    searchQuery = "SELECT Customer.customer_id, Customer.fullName, Customer.meter_number, Bills.bill_id, Bills.billing_month, Bills.units_used, Bills.rate_per_unit, Bills.total_amount FROM Bills INNER JOIN  Customer ON Bills.customer_id = Customer.customer_id WHERE Customer.meter_number = %s"
    mycursor.execute(searchQuery,Meter_Nnumber)
    customers = mycursor.fetchall()
    header = ["Customer_id","Full Name","Meter number", "Bill ID","Billing Month","units_used","Rate","Total Amount (₦)"]
    print(tabulate(customers,headers=header, tablefmt="fancy_grid"))
view_bills()