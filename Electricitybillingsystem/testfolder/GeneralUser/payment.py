import pymysql
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


def pay_card():
    print("payment through card")
    meter_number = input("input meter number: ")
    query = "SELECT  Bills.total_amount FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
    mycursor.execute(query,(meter_number))
    bills = mycursor.fetchall()
    for bill in bills:
        print(f"your bill is ₦{bill}")
    bill_month = input("billing month: ")
    cardNumber = input("\ninput card number: ")
    expirydate = input("input EndDate: ")
    CVC = input("input CVC number: ")
    amount = input("amount to pay: ")

    getBill_id = "SELECT  Bills.bill_id FROM Bills JOIN Customer ON Bills.customer_id = Customer.customer_id where meter_number = %s"
    mycursor.execute(getBill_id,(meter_number))

    mybills = mycursor.fetchone()
    
    bill_id = mybills[0]

    bill_Query = "INSERT INTO Payments (bill_id, amount_paid, payment_method,billing_month,Payment_STATUS ) VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(bill_Query,(bill_id,amount,"CARD",bill_month,"PAYED"))
    mydb.commit()
    print(f"✅ Bill  for {meter_number} | Amount payed: ₦{amount} Payed succesfully")

   



#payment menu
def payment_menu():
    print("Select a payment method")
    print("\n")
    print("1.Pay with card 💳 ")
    print("2.pay with transfer ")
   
    selection = input("select an option: ")
    if selection == "1":
        pay_card()
    if selection == "2":
        pass









def payment():
    print("1.pay bills")
    print("2.Generate Reciept")
    print("3.Exit")

    option = input("select an option: ")

    if option == "1":
        payment_menu()
    elif option == "2":
        pass
    elif option == "3":
        return
    else:
        print("invalid")

payment()