#import database  connector for python
import pymysql

#connect to db
connection = pymysql.connect(
    host="localhost",
    port=3307,
    user="root",
    password="09155564452",
    database="company_db"

)

#create a cursor object using the connector
cursor = connection.cursor()

#define the select query
select_query = "SELECT * FROM employees "

#execute the query
cursor.execute(select_query)

#fetch all rows from the result
employees = cursor.fetchall()

for employee in employees:
  
    print(f" Name: {employee[1]}, lastname :{employee[2]}, email :{employee[3]}")

#inserting data a
insert_data = ("")    
   