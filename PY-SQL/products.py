import pymysql      #pip install pymysql before writing and running the codes

def connect_db():
    # Connect to MariaDB
    connection = pymysql.connect(
        host="localhost",         # MariaDB host
        port=3307,                # Port where MariaDB is running (default is 3306)
        user="pydb_user",         # MariaDB username
        password="userpassword",   # MariaDB password
        database="ecom_db"        # Your database name
    )
    return connection

    # Create a cursor object using the connection
    #cursor = connection.cursor()

# Function to close the connection
def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed.")

def display_products(connection):
    # Create a cursor object using the connection
    cursor = connection.cursor()
    
    # Define the SELECT query
    select_query = "SELECT * FROM products"

    # Execute the query
    cursor.execute(select_query)

    # Fetch all rows from the result
    products = cursor.fetchall()

    # Display the results
    for product in products:
        print(f"Name: {product[1]}, Price: {str(product[2])}, Category Id: {product[3]}")


def insert_product(connection):
    #To insert data into the table, we use an INSERT INTO SQL query
    # Define an INSERT query
    insert_query = "INSERT INTO products (name, price, category_id) VALUES (%s, %s, %s)"

    # Data to insert
    data = ("V-neck T-shirt 2X", 200.50, 2)

    # Create a cursor object using the connection
    cursor = connection.cursor()

    # Execute the insert query with data
    cursor.execute(insert_query, data)

    # Commit the transaction to make changes permanent
    connection.commit()

    print(f"Product {data[0]} added successfully.")  


def update_product(connection):
    # To update an existing record, use an UPDATE SQL query.
    # Define an UPDATE query
    update_query = "UPDATE products SET price = %s WHERE id = %s"

    # Data to update
    new_price = 85.00
    product_id = 5

    # Create a cursor object using the connection
    cursor = connection.cursor()
    # Execute the update query
    cursor.execute(update_query, (new_price, product_id))

    # Commit the transaction
    connection.commit()

    print(f"Data updated for product with ID {product_id}.")


def delete_product(connection):
    # To delete a record, use a DELETE SQL query.
    # Define a DELETE query
    delete_query = "DELETE FROM products WHERE id = %s"

    # Employee ID to delete
    product_id_to_delete = 6

    # Create a cursor object using the connection
    cursor = connection.cursor()

    # Execute the delete query
    cursor.execute(delete_query, (product_id_to_delete,))

    # Commit the transaction
    connection.commit()

    print(f"Product with ID {product_id_to_delete} deleted.")

def main_app():
        connection = connect_db()    # Establishing connection

        if connection is None:
            return 
        
        while True:
            print("Menu ")
            print("1. Display product")
            print("2. Insert product")
            print("3. Update product")
            print("4. Delete product")
            print("0. Exit product")
            choice = input("Enter selection: ")
            if choice == "1":            
                display_products(connection)
            elif choice == "2":
                insert_product(connection)
            elif choice == "3":
                update_product(connection)
            elif choice == "4":
                delete_product(connection)
            elif choice == "0":
                print("Bye")
                close_connection(connection)
                break  
            else:
                print("wrong choice")  


if __name__ == "main":
    main_app()