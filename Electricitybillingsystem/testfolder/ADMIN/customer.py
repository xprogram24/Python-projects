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

#function to add customer
addCustomer_query = "INSERT INTO Customer (fullName, meter_number, address, phoneNumber, email) VALUES (%s,%s,%s,%s,%s)"
def addCustomer():
   fullname =  input("Please input customers full name: ").strip().lower()
   meterNumber = input("Input meter number: ").strip()
   address = input("Customer address: ").strip().lower()
   phoneNumber = input("Input phone number: ").strip()
   email = input("Enter the email you would live to use:" ).strip().lower()

   mycursor.execute(addCustomer_query, (fullname,meterNumber,address,phoneNumber,email)) 

   mydb.commit()
   print("user creation successfull")

  
#addCustomer()

# function to view customers
def viewCustomer():
    while True:
        print("1.Search a customer by meter number")
        print("2.view all customers")
        print("3.Exit")
        option = input("\nselect an option: ")

        if option == "1":
            search = input("input meter Number: ").strip()
            searchQuery = "SELECT customer_id,meter_number,fullName,address,phoneNumber,email FROM Customer WHERE meter_number LIKE %s"
            mycursor.execute(searchQuery,("%" + search +"%"))

            customers = mycursor.fetchall()
            if customers:
                headers = ["customer ID",  "Meter Number","fullname", "Address", "Phone Number", "Email"]
                print(tabulate(customers,headers=headers, tablefmt="fancy_grid"))
            else:
                print("print customer doesnt exist")
        


        elif option == "2":
            print("list of customers available")
            viewCustomer_query = "SELECT customer_id,meter_number,fullName,address,phoneNumber,email FROM Customer"
            mycursor.execute(viewCustomer_query)

            customers = mycursor.fetchall()
   
            headers = ["customer ID",  "Meter Number","fullname", "Address", "Phone Number", "Email"]
            print(tabulate(customers,headers=headers, tablefmt="fancy_grid"))
            

        elif option == "3":
            print("exiting view customer")
            break
            
            
#viewCustomer()

#function to update customer
def updateCustomer():
    request = input("\nWhat do you want to change (Fullname , address ,phone number or email): ").strip().lower()
    meterNumber = input("please input meter Number: ").strip()
    searchQuery = "SELECT customer_id,meter_number,fullName,address,phoneNumber,email FROM Customer WHERE meter_number LIKE %s"
    mycursor.execute(searchQuery, ("%" + meterNumber + "%",))


    customers = mycursor.fetchall()
    headers = ["customer ID",  "Meter Number","fullname", "Address", "Phone Number", "Email"]
    print(tabulate(customers,headers=headers, tablefmt="fancy_grid"))

    if request == "fullname":
        new_name = input("input new name: ")
        updateQuery = "UPDATE Customer SET fullName = %s WHERE meter_number = %s"
        mycursor.execute(updateQuery, (new_name,meterNumber))
        mydb.commit()
        print("successfully updated")

    elif request == "address":
        new_Address = input("input new Address: ")
        updateQuery = "UPDATE Customer SET address = %s WHERE meter_number = %s"
        mycursor.execute(updateQuery, (new_Address,meterNumber))
        mydb.commit()
        print("successfully updated")

    elif request == "phone number":
        new_phoneNumber = input("input new phone number: ")
        updateQuery = "UPDATE Customer SET phoneNumber = %s WHERE meter_number = %s"
        mycursor.execute(updateQuery, (new_phoneNumber,meterNumber))
        mydb.commit()
        print("successfully updated")

    elif request == "email":
        new_email = input("input new email: ")
        updateQuery = "UPDATE Customer SET email = %s WHERE meter_number = %s"
        mycursor.execute(updateQuery, (new_email,meterNumber))
        mydb.commit()
        print("successfully updated")
    else:
        return 

#updateCustomer()
    