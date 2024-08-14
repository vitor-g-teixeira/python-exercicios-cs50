from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", size=48)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        self.ln(20)

    def print_name(self, name):
        self.set_font("helvetica", size = 28)
        self.set_text_color(255, 255, 255)
        self.cell(0, pdf.h/2 + 180/4, name + " took CS50", align="C")

pdf = PDF()

name = input("Name: ")
image_path = "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png"
pdf.add_page()
pdf.image(image_path, x = (pdf.w - 180)/2, y = pdf.h/2 - 180/2, w = 180, h = 180, keep_aspect_ratio = True)
pdf.print_name(name)
pdf.output("shirtificate.pdf")
