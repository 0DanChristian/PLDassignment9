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
        resume.image('respic.png', 170, 8, 35)
        resume.set_font('arial', 'B', 29)
        resume.cell(0, 12, 'DAN CHRISTIAN PIÑERO', align = 'C', ln=1)
        resume.ln(25)                                                                   # note: 'In' is the spaces in between
