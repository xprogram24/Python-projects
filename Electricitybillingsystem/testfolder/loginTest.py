#testing login

#for regular users, create column for password, learn how to use hashing, 
#user enters gmail and password.
#if the gmail is not found they go to admin to create to get a registered

#if gmail and password exist grant login
#if gmail exist but password doesnt exist aask them to create a password

#if they forgot password ( optional )





'''hash_object.update(b"mypassword1234")
hex_digest = hash_object.hexdigest()

print(hex_digest)'''


'''mypassword = input("input password")
hased_password = hashlib.sha256(mypassword.encode()).hexdigest()
print(hased_password)'''
import hashlib
import pymysql
#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'GeneralUser')))
# Now you can import modules from 'anotherfolder'
# Example: from mymodule import myfunction
from mainUser import menu

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="admin",
    password = "myadmin",
    database="electricBilling_DB"
)

mycursor = mydb.cursor()
print("connection successful")

#testing input password
'''query  = "UPDATE  Customer SET User_password = %s Where email = 'mikelobi@gmail.com' "
password = "mikleobi123"
hased_password = hashlib.sha256(password.encode()).hexdigest()
mycursor.execute(query,(hased_password))
mydb.commit()
print("change commited sucessfully")'''






def login():
    email = input("input your email: ").strip().lower()
    confirmQuery = "SELECT User_password from Customer WHERE Email = %s"
    mycursor.execute(confirmQuery,(email))
    pa = mycursor.fetchone()


    if pa:
        mypassword = pa[0]
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
                menu()
            else:
                    print("wrong password")
    else:
        print("email not found")

login()