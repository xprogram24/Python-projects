#import database  connector for python
import pymysql

#connect to db
connection = pymysql.connect(
    host="localhost",
    port=3307,
    user="root",
    password="09155564452",
    database="ecom_db"

)

#create a cursor object using the connector
cursor = connection.cursor()

#define the select query
select_query = "SELECT * FROM products "

#execute the query
cursor.execute(select_query)

#fetch all rows from the result
products = cursor.fetchall()

for product in products:
    print(product)
    print(f" Name: {product[1]} price: {products[2]} catergory_id: {products[3]}")