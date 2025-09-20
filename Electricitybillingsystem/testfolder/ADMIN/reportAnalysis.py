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

def Totalrevenue():
    query = "SELECT SUM(amount_paid) FROM PAYMENTS"
    mycursor.execute(query)
    rev = mycursor.fetchone()
    total_revenue = rev[0]
    print(f"Total Revenue collected : NGN {total_revenue}")
    


def outstanding_balance():
    query = "SELECT SUM(total_amount)  FROM Bills WHERE payment_STATUS = %s "
    mycursor.execute(query,("unpaid",))
    unpaid = mycursor.fetchone()
    outstanding = unpaid[0]
    print(f"Outstanding is NGN {outstanding}")


def monthly_usage():
    query = """
    SELECT billing_month, 
           COALESCE(SUM(units_used), 0), 
           COALESCE(SUM(total_amount), 0)
    FROM Bills
    GROUP BY billing_month
    ORDER BY billing_month
"""
    mycursor.execute(query)
    monthly_trend = mycursor.fetchall()

    print("\n Monthly Usage Trend")
    print("\n MONTHLY USAGE TREND")
    if monthly_trend:
        print(tabulate(monthly_trend, headers=["Month", "Total Units", "Total Amount (NGN)"], tablefmt="fancy_grid"))
    else:
        print("No monthly usage data available.")

