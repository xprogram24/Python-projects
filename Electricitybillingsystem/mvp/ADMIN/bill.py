#add try catch to gracefully catch error
import pymysql
import time
from tabulate import tabulate
try :
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
        meter_number = input("please input meter number :").strip()
        
        mycursor.execute("SELECT * FROM Customer WHERE meter_number = %s", (meter_number))
        result = mycursor.fetchall()

        if result:
            query = "SELECT customer_id FROM Customer WHERE meter_number = %s"
            mycursor.execute(query,meter_number)

            #ADD an if statement to check if meter number exists
            customers = mycursor.fetchone()
        
            customer_id = customers[0]

            billing_month = input("input billing month: ").strip()
            unit = int(input("input unit consumed: "))
            rate = 66.00
        
            bill = unit * rate 
            VAT = 0.075 * bill
            total_amount = bill + VAT
            print(f"bill is {bill}")
            print(f"total bill + vat is {total_amount}")
            bill_query = "INSERT INTO Bills (customer_id, units_used, rate_per_unit, total_amount, billing_month,Payment_STATUS) VALUES (%s,%s,%s,%s,%s,'unpaid')"
            mycursor.execute(bill_query,(customer_id,unit,rate,total_amount,billing_month))
            mydb.commit()
            time.sleep(2)
            print(f"✅ Bill generated for {meter_number} | Amount: ₦{total_amount} ")
        else:
            print("meter number does not exist")

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
            header = ["Customer_id","Full Name","Meter number", "Bill ID","Billing Month","units_used","Rate (#)","Total Amount (#)","Payment_STATUS"]
            print(tabulate(customers,headers=header, tablefmt="fancy_grid"))

    def view_bills():
        #add an if to check if meter number exist
        while True:
            print("\n1.view all bills")
            print("2.View a specific bill")
            print("3.EXIT")

            option = input("select an option: ").strip()
            if option == "1":
                searchQuery = "SELECT Customer.customer_id, Customer.fullName, Customer.meter_number, Bills.bill_id, Bills.billing_month, Bills.units_used, Bills.rate_per_unit, Bills.total_amount,Bills.Payment_STATUS FROM Bills INNER JOIN  Customer ON Bills.customer_id = Customer.customer_id "
                mycursor.execute(searchQuery)
                customers = mycursor.fetchall()
                time.sleep(1)
                header = ["Customer_id","Full Name","Meter number", "Bill ID","Billing Month","units_used","Rate","Total Amount (#)","Payment_STATUS"]
                print(tabulate(customers,headers=header, tablefmt="fancy_grid"))
        
            elif option == "2": 
                Meter_Nnumber = input("input meter Number: ").strip()
                mycursor.execute("SELECT * FROM Customer WHERE meter_number = %s", (Meter_Nnumber))
                result = mycursor.fetchall()

                if result:
                    searchQuery = "SELECT Customer.customer_id, Customer.fullName, Customer.meter_number, Bills.bill_id, Bills.billing_month, Bills.units_used, Bills.rate_per_unit, Bills.total_amount,Bills.Payment_STATUS FROM Bills INNER JOIN  Customer ON Bills.customer_id = Customer.customer_id WHERE Customer.meter_number LIKE  %s"
                    mycursor.execute(searchQuery,("%" + Meter_Nnumber + "%"))
                    customers = mycursor.fetchall()
                    time.sleep(1)
                    header = ["Customer_id","Full Name","Meter number", "Bill ID","Billing Month","units_used","Rate","Total Amount (#)","payment Status"]
                    print(tabulate(customers,headers=header, tablefmt="fancy_grid"))
                else:
                    print("meter number not found")

            elif option == "3":
                print("thank you for using bill managment")
                break
            else:
                print("invalid")

except Exception as e:
    print("Database connection failed",e)



    
