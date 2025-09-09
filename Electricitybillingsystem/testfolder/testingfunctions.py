from datetime import datetime

current_datetime =  datetime.now()
print(current_datetime)
day = current_datetime.date()

#fetch bill from meter number
import time
from reportlab.lib.pagesizes import letter


def generate_reciept():
    print("\t\t\t\t\t\t\tExcel power distribution company (E-PDC) RECIEPT")
    print("\nYour payment was successful")
    print("--------------------------------------------------------------------------------------------------")
    print("\nYour transaction details as follows")
    print("Meter number: hel147896")
    print("--------------------------------------------------------------------------------------------------")
    print("\nCustomer Name                                        ADEBAYO PAUL")
    print("\nAddress                                              11 BOLA AHMED STREET, IKEJA")  
    print("\nService Name:                                        Excel power distribution company (E-PDC")
    print("\nMeter Number                                         hel147896")
    print("\nAmount                                               #35,000")
    print("\nVAT                                                  7.5%")
    print("\nTotal amount Paid                                    #35,200")
    print("\npayment ID                                           15")
    print("\nStatus                                               PAID")
    print(f"\nDate                                                {day}")
    print("--------------------------------------------------------------------------------------------------")
    print("\n                               THANK YOU FOR USING E-Electricity")
#generate_reciept()

def myMeternumber():
   global x 
   x = 15
   return x

def result():
    myMeternumber()
    print(x)

result()

