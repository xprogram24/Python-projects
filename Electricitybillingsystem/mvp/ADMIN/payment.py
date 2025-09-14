import pymysql
import time
from tabulate import tabulate
from fpdf import FPDF
mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="admin",
    password = "myadmin",
    database="electricBilling_DB"
)
mycursor = mydb.cursor()
print("db successfully connected to ")

#function for admin view payment
def view_payment():
    view_Query = "SELECT Customer.fullName, Customer.meter_number, Bills.billing_month,Bills.units_used,Bills.total_amount,Payments.billing_month,Payments.date_of_payment,Payments.amount_paid,Payments.Payment_STATUS FROM Customer INNER JOIN Bills ON Customer.customer_id = Bills.customer_id INNER JOIN Payments ON Bills.bill_id = Payments.bill_id"
    mycursor.execute(view_Query)
    payment = mycursor.fetchall()
    time.sleep(3)
    Header = ["Customer name","METER NUMBER","BILL MONTH","UNIT USED","TOTAL AMOUNT (₦)","MONTH PAYED","DATE ","AMOUNT PAYED (₦)","STATUS"]
    print(tabulate(payment,headers=Header,tablefmt="fancy_grid"))




def generatepdf():
    query = '''SELECT Customer.fullName, Customer.meter_number, Customer.address,
           Bills.billing_month, Bills.units_used, Bills.total_amount,
           Payments.billing_month, Payments.date_of_payment, Payments.amount_paid,
           Payments.Payment_STATUS, Payments.payment_id
           FROM Customer 
           INNER JOIN Bills ON Customer.customer_id = Bills.customer_id 
           INNER JOIN Payments ON Bills.bill_id = Payments.bill_id 
           WHERE Customer.meter_number = %s 
           ORDER BY Payments.date_of_payment DESC LIMIT 1'''
    
    meter_number = input("input meter number")
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

    pdf.output("report.pdf")
    print("saved")

    
def tracking():
    print("1.track paid")
    print("2.unpaid")
    print("3.exit")

    selection = input("click option: ")
    if selection == "1":
        
        view_Query = '''SELECT Customer.fullName, Customer.meter_number, 
                        Bills.billing_month,Bills.units_used,Bills.total_amount,
                        Bills.payment_STATUS
                        FROM Customer INNER JOIN Bills ON 
                        Customer.customer_id = Bills.customer_id 
                         WHERE Bills.payment_STATUS = "PAYED" '''
        mycursor.execute(view_Query)
        customers = mycursor.fetchall()
        header = ["Full Name","Meter number","Billing Month","units_used","Total Amount (#)","Date","Payment_STATUS"]
        print(tabulate(customers,headers=header, tablefmt="fancy_grid"))
      
  
    elif selection == "2":
        view_Query = '''SELECT Customer.fullName, Customer.meter_number, 
                        Bills.billing_month,Bills.units_used,Bills.total_amount,
                        Bills.payment_STATUS
                        FROM Customer INNER JOIN Bills ON 
                        Customer.customer_id = Bills.customer_id 
                         WHERE Bills.payment_STATUS = "unpaid" '''
        mycursor.execute(view_Query)
        customers = mycursor.fetchall()
        header = ["Full Name","Meter number","Billing Month","units_used","Total Amount (#)","Date","Payment_STATUS"]
        print(tabulate(customers,headers=header, tablefmt="fancy_grid"))
    elif selection == "3":
        return
    else:
        print("invalid")




