# from PyPDF2 import pdfWriter
# import os
# merger = pdfWriter()
# file = [file for file in os.listdir() if file.endswith(".pdf")]
# for pdf in file:
#     merger.append(pdf)
# merger.write("Mypdf.pdf")
# merger.close()
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()