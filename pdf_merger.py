import pypdf
#from pypdf import pdfWriter
import os

merger = pypdf.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combined.pdf")