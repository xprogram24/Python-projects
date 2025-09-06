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
print("db successfully connected to ")
def view_payment():
    view_Query = "SELECT Customer.fullName, Customer.meter_number, Bills.billing_month,Bills.units_used,Bills.total_amount,Payments.billing_month,Payments.date_of_payment,Payments.amount_paid,Payments.Payment_STATUS FROM Customer INNER JOIN Bills ON Customer.customer_id = Bills.customer_id INNER JOIN Payments ON Bills.bill_id = Payments.bill_id"
    mycursor.execute(view_Query)
    payment = mycursor.fetchall()

    Header = ["Customer name","METER NUMBER","BILL MONTH","UNIT USED","TOTAL AMOUNT (₦)","MONTH PAYED","DATE ","AMOUNT PAYED (₦)","STATUS"]
    print(tabulate(payment,headers=Header,tablefmt="fancy_grid"))
view_payment()

def Generate_Reciept():
    pass
