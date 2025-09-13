import hashlib
import pymysql

from mainUser import menu

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="customer",
    password = "mycustomer",
    database="electricBilling_DB"
)

mycursor = mydb.cursor()
print("connection successful")

def login():
    email = input("input your email: ").strip().lower()
    confirmQuery = "SELECT User_password , meter_number from Customer WHERE Email = %s"
    mycursor.execute(confirmQuery,(email,))
    pa = mycursor.fetchone()


    if pa:
        mypassword,meter_number = pa
        if mypassword is None:
            print("no password set please create one")
            mypassword = input("input the password you would like to use: ").strip()
            hashed_password = hashlib.sha256(mypassword.encode()).hexdigest()
            query  = "UPDATE  Customer SET User_password = %s Where email = %s "
            mycursor.execute(query,(hashed_password,email))
            mydb.commit()
            print("password successfully created")
        else :
            testpassword = input("input password: ").strip()
            hased_testpassword = hashlib.sha256(testpassword.encode()).hexdigest()    

            if hased_testpassword == mypassword:
                print("login succesful")

                menu(meter_number)
            else:
                    print("wrong password")
    else:
        print("email not found")

login()