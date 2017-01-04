# Python3.5
# combinepdfs.py
# _______________

import PyPDF2
import os

# Get all the PDF filenames.
# Store in the pdf_files list.
pdf_files = []
for file in os.listdir('.'):
    if file.endswith('.pdf'):
        pdf_files.append(file)
pdf_files.sort()
print (pdf_files)
# Sort the PDF files 

# Create an object of the PdfFileWriter()class from the PyPDF2 module
pdf_writer = PyPDF2.PdfFileWriter()

# Iterate through all the PDFs.
for file in pdf_files:
    pdf_obj = open(file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_obj)

    # Loop through all pages of the PDFs and append them.
    
    # If you wish to skip the first page of the PDF, you can use:
    #for pageNum in range(1, pdfReader.numPages):
    
    # In general, to skip the first 'n' pages, use:
    #for pageNum in range(n, pdfReader.numPages):
    
    for page_no in range(0, pdf_reader.numPages): #no skipping (0)
        page = pdf_reader.getPage(page_no)
        pdf_writer.addPage(page)

# Save the resulting PDF to a file.
pdf_output = open('CombinedPDFs.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
