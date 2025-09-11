import pymysql

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="09155564452", 
    database="mydatabase"
)

mycursor = connection.cursor()

#Query = "CREATE DATABASE mydatabase"
#Query = "SHOW TABLES"
#Query = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
Query = "INSERT INTO CUSTOMERS (name, address) VALUES (%s,%s)"
val = [
    ("john","highwaya 21"),
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]
#Query = "select * from customers "
#Query = "SELECT * FROM customers ORDER BY address ASC "
#Query = "DELETE FROM customers  "
mycursor.executemany(Query,val)

connection.commit()

print(mycursor.rowcount,"records added")




customers = mycursor.fetchall()
print(customers)
#for customer in customers:
#    print(customer)


