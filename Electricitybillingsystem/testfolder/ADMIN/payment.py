import pymysql

from tabulate import tabulate
mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="admin",
    password = "myadmin",
    database="electricBilling_DB"
)

def view_payment():
    pass

def Generate_Reciept():
    pass
