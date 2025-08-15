import pymysql

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="09155564452",
    database="mydatabase"
)

mycursor = mydb.cursor()

query = "DROP TABLE IF EXISTS customers"

mycursor.executemany(query)

mydb.commit()

print("db table dropped")