from fpdf import FPDF

# Create PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="POLYSIA PVT. LTD. LEADERSHIP AND OWNERSHIP AGREEMENT", ln=True, align="C")
pdf.ln(10)

# Table in PDF format
pdf.set_font("Arial", 'B', 12)

# Column headers
headers = ['Section', 'Details']
col_widths = [50, 140]

# Set up table headers
for i, header in enumerate(headers):
    pdf.cell(col_widths[i], 10, header, border=1, align="C")
pdf.ln()

# Data for the table
data = [
    ["Parties Involved", "Karmanya Tyagi (CEO), Neeraj Tyagi (Director), Ritu Tyagi (Director), CFO and CTO (To be hired)"],
    ["Date of Agreement", "___ day of ______, 2024"],
    ["Company Name", "Polysia Pvt. Ltd."],
    ["Ownership Structure", 
     "- Karmanya Tyagi (CEO) – 51% \n- Neeraj Tyagi (Director) – 12.5% \n- Ritu Tyagi (Director) – 12.5% \n- CFO – 12% (upon hiring) \n- CTO – 12% (upon hiring)"],
    ["Roles & Responsibilities", 
     "Directors (Neeraj Tyagi & Ritu Tyagi): \n- Corporate Governance \n- Financial Oversight \n- Strategic Guidance \n- Risk Management \n- Stakeholder Relations \n\n" 
     "CEO (Karmanya Tyagi): \n- Lead company’s vision and mission \n- Oversee operations \n- Develop long-term strategies \n- Represent Polysia publicly \n\n"
     "CFO (To be hired): \n- Lead financial strategy \n- Manage budgeting and reporting \n- Collaborate with CEO and Directors on financial decisions \n\n"
     "CTO (To be hired): \n- Oversee technology and product development \n- Ensure technological solutions meet industry standards"],
    ["Signatures", 
     "Karmanya Tyagi, CEO \nNeeraj Tyagi, Director \nRitu Tyagi, Director \nCFO (To be hired) \nCTO (To be hired)"],
]

# Populate table with data
pdf.set_font("Arial", '', 12)
for row in data:
    for i, item in enumerate(row):
        pdf.multi_cell(col_widths[i], 10, item, border=1, align="L")
    pdf.ln()

# Save PDF document
pdf_output_path = "/mnt/data/Polysia_Leadership_Agreement_Table.pdf"
pdf.output(pdf_output_path)

pdf_output_path

