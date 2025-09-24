from fpdf import FPDF
import pymysql
import time
#from tabulate import tabulate
from datetime import datetime

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="customer",
    password = "mycustomer",
    database="electricBilling_DB"
)

mycursor = mydb.cursor()
month = "january"
def quer(meter_number = "hel225967" ):
    query = '''SELECT Customer.fullName, Customer.meter_number, Customer.address,
           Bills.billing_month, Bills.units_used, Bills.total_amount,
           Payments.billing_month, Payments.date_of_payment, Payments.amount_paid,
           Payments.Payment_STATUS, Payments.payment_id
           FROM Customer 
           INNER JOIN Bills ON Customer.customer_id = Bills.customer_id 
           INNER JOIN Payments ON Bills.bill_id = Payments.bill_id 
           WHERE Customer.meter_number = %s 
           ORDER BY Payments.date_of_payment DESC LIMIT 1'''

    mycursor.execute(query,meter_number)
    customer = mycursor.fetchone()
    
    if not customer:
        print("❌ No payment record found for this meter number.")
        return
    


    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)
    pdf.set_font("helvetica", 'B', 14)
    pdf.cell(200, 10,"Excel Power Distribution Company (E-PDC) RECEIPT" , new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(10)
    pdf.cell(200, 10,"Transaction Details:", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.cell(200, 10, f"Customer Name:                              {customer[0]}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200, 10, f"Meter Number:                                 {customer[1]}", new_x="LMARGIN", new_y="NEXT")
    
    
    pdf.cell(200, 10,"--------------------------------------------------------------------------------",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200, 10,"Your payment was successful ",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,"---------------------------------------------------------------------------------",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,"Transaction Details:",new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.cell(200,10,f"Customer Name:                              {customer[0]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"Meter Number:                                 {customer[1]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"Address:                                          {customer[2]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"Billing Month:                                  {customer[6]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"Units Used:                                      {customer[4]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"Total Bill:                                          NGN{customer[5]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"Amount Paid:                                   NGN{customer[8]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"VAT:                                                  7.5%",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"Payment ID:                                      {customer[10]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"Payment Status:                              {customer[9]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,f"Date of Payment:                             {customer[7]}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,"---------------------------------------------------------------------------------",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200,10,"THANK YOU FOR USING E-Electricity ",new_x="LMARGIN", new_y="NEXT",align="L")
    pdf.ln(5)

    pdf.output(f"report {month}.pdf")
    print("saved")

quer()