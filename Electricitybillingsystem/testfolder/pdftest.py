from fpdf import FPDF

def generate_receipt_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Header
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Excel Power Distribution Company (E-PDC) RECEIPT", ln=True, align="C")
    pdf.ln(10)

    # Transaction Details
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Transaction Details:", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, f"Customer Name:  Adeboywa ", ln=True)
    pdf.cell(200, 10, f"Meter Number: hel343456", ln=True)
    pdf.cell(200, 10, f"Address: 17 AKIN STREET", ln=True)
    pdf.cell(200, 10, f"Billing Month: JANUARY", ln=True)
    pdf.cell(200, 10, f"Units Used: 200", ln=True)
    pdf.cell(200, 10, f"Total Bill: ₦5000", ln=True)
    
    pdf.cell(200, 10, f"Amount Paid: ₦4,900", ln=True)
    pdf.cell(200, 10, f"VAT: 7.5%", ln=True)
    pdf.cell(200, 10, f"Payment ID: 1", ln=True)
    pdf.cell(200, 10, f"Payment Status: PAYED", ln=True)
    pdf.cell(200, 10, f"Date of Payment: CASH", ln=True)

    # Save the PDF
    pdf.output("receipt.pdf")
    print("✅ Receipt saved as receipt.pdf")
generate_receipt_pdf()