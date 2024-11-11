# Let's retry generating the enhanced PDF with the provided logo, roles, and responsibilities.

from fpdf import FPDF

class PDFWithLogo(FPDF):
    def header(self):
        # Add the logo at the top-left corner
        self.image("/mnt/data/POLYSIA.png", x=10, y=8, w=30)
        self.set_font("Arial", "B", 20)
        self.set_text_color(0, 102, 204)  # Blue color for the title
        self.cell(0, 10, "PolysiaTech Pvt. Ltd. - Ownership Structure", ln=True, align="C")
        self.ln(5)
        self.set_font("Arial", "I", 12)
        self.cell(0, 10, "Effective from March 2025", ln=True, align="C")
        self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.set_text_color(128, 128, 128)  # Gray color for the footer
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_ownership_section(self, owner, role, percentage, responsibilities, color):
        self.set_text_color(*color)
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, f"{owner} ({role}) - {percentage} ownership", ln=True)
        self.ln(5)
        
        self.set_font("Arial", "", 12)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 10, f"Responsibilities:\n{responsibilities}")
        self.ln(10)

# Create the PDF with the logo, roles, and responsibilities
pdf = PDFWithLogo()
pdf.add_page()

# Ownership details with colors and responsibilities
ownership_data = [
    ("Karmanya Tyagi", "CEO", "51%", "Overall company strategy, vision, and leadership. Responsible for business growth and stakeholder management.", (0, 153, 76)),  # Green
    ("Neeraj Tyagi", "Director", "12.5%", "Overseeing business operations, ensuring compliance, and supporting strategic decisions.", (255, 153, 51)),  # Orange
    ("Ritu Tyagi", "Director", "12.5%", "Managing client relations, enhancing partnerships, and driving business expansion.", (204, 0, 102)),  # Pink
    ("CFO", "Chief Financial Officer", "12%", "To be allocated upon hiring. Will manage financial planning, risk management, and investment strategies.", (51, 102, 255)),  # Blue
    ("CTO", "Chief Technology Officer", "12%", "To be allocated upon hiring. Will lead technology strategy, innovation, and digital transformation.", (102, 0, 204))  # Purple
]

# Add each section to the PDF
for owner, role, percentage, responsibilities, color in ownership_data:
    pdf.add_ownership_section(owner, role, percentage, responsibilities, color)

# Save the PDF to a file with an updated design
pdf_path_with_logo = "/mnt/data/PolysiaTech_Ownership_Structure_Enhanced.pdf"
pdf.output(pdf_path_with_logo)

pdf_path_with_logo

