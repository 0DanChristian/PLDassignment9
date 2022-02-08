# Assignment 9

# PDF Resume Creator
#	- Create a python program that will create your personal resume in PDF format
#	- All personal details are stored in a JSON file
#	- Your program should read the JSON file and write the details in the PDF
#	- The output file should be: LASTNAME_FIRSTNAME.pdf

# Steps:
# 1. Install necessary extensions.
# 2. Set-up both .json and .py files.
# 3. Set-up the code that will convert the .json file into a .pdf file
# 4. Format the final output

from fpdf import FPDF
from ctypes import alignment 
import json

# header
class PDF(FPDF):
    def header(resume):
        resume.image('respic.png', 170, 8,39)
        resume.set_font('arial', 'BU', 29)
        resume.cell(0, 12, 'DAN CHRISTIAN PIÑERO', align = 'L', ln=1)
        resume.set_font('arial', '', 15)
        resume.cell(0,12, 'Customer Service Manager', align = 'L')
        resume.ln(25)                                                                   # note: 'In' is the spaces in between

# PDF Format
pdf = PDF('P', 'mm', "Letter")
pdf.set_auto_page_break(auto=1, margin=30)
pdf.add_page() 

# custom fonts
pdf.add_font('Serif', '',
                    r"E:\\Desktop\\font\\serif I\\static\\SourceSerif4_18pt\\SourceSerif4_18pt-Black.ttf",
                    uni=True)
                    
pdf.add_font('Serif', 'B',
                    r"E:\\Desktop\\font\\serif I\\static\\SourceSerif4_18pt\\SourceSerif4_18pt-Bold.ttf",
                    uni=True)

pdf.add_font('Serif', 'BI',
                    r"E:\\Desktop\\font\\serif I\\static\\SourceSerif4_18pt\\SourceSerif4_18pt-BoldItalic.ttf",
                    uni=True)

# Resume Information
resume_source = open('resume.json', 'r')
PDFc = resume_source.read()
resume_data = json.loads(PDFc)

# Data
for data in resume_data:
    pdf.ln(5)
    pdf.set_font('Serif', 'B', 15)
    pdf.cell(0, 10, f"{data['header1']}", 'BU', ln=1)
    pdf.ln(3)  

    # personal info
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"Name: {data['Name']}", align='L', ln=1)
    pdf.cell(0, 5, f"Address: {data['Address']}", align='L', ln=1)
    pdf.cell(0, 5, f"Contact No.: {data['Contact No.']}", align='L', ln=1)
    pdf.cell(0, 5, f"Email: {data['Email']}", align='L', ln=1)
    pdf.ln(0)

    # header 2
    pdf.set_font('Serif', 'B', 15)
    pdf.cell(0, 10, f"{data['header2']}", 'BU', ln=1)
    pdf.ln(3)
    pdf.set_font('Serif', '', 10)
    pdf.multi_cell(0, 5, f"{data['OBJECTIVES']}", align='L', ln=1)
    pdf.ln(1)

    # header 3
    pdf.set_font('Serif', 'B', 15)
    pdf.cell(0, 10, f"{data['header3']}", 'BU', ln=1)
    pdf.ln(3)

    # Course
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, "Course:", align='L', ln=1)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"{data['Course']}", align='L', ln=1)
    pdf.ln(3)

    # University
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, "University:", align='L', ln=1)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"{data['University']}", align='L', ln=1)
    pdf.ln(3)

    # Relevant Coursework
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, "Relevant Coursework:", align='L', ln=1)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"{data['Relevant Coursework']}", align='L', ln=1)
    pdf.ln(3)

    # header 4 (work exp)
    pdf.set_font('Serif', 'B', 15)
    pdf.cell(0, 10, f"{data['header4']}", 'BU', ln=1)
    pdf.ln(5)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"{data['Work1']}", align='L', ln=1)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"{data['Company1']}", align='L', ln=1)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"{data['Years of Working']}", align='L', ln=1)
    pdf.ln(3)

    # header 5 (skills)
    pdf.set_font('Serif', 'B', 15)
    pdf.cell(0, 10, f"{data['header5']}", 'BU', ln=1)
    pdf.ln(3)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"- {data['Skill1']}", align='L', ln=1)
    pdf.cell(0, 5, f"- {data['Skill2']}", align='L', ln=1)
    pdf.ln(3)

    # header 6 (refs)
    pdf.set_font('Serif', 'B', 15)
    pdf.cell(0, 10, f"{data['header6']}", 'BU', ln=1)
    pdf.ln(3)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"{data['REFERENCE']}", align='L', ln=1)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"{data['Occupation']}", align='L', ln=1)
    pdf.set_font('Serif', '', 10)
    pdf.cell(0, 5, f"{data['Contact']}", align='L', ln=1)
    pdf.ln(3)

    # name
#    pdf.set_font('arial', 'U', 8)
#    pdf.set_x(20)
#    pdf.cell(0, 0, f"{data['Footer']}", align='R')
    pdf.image('name.png', 167, 265, 60)

    # signature
    pdf.image('signature.png', 167, 220, 50)




pdf.output('Dan_Christian_resume.pdf')