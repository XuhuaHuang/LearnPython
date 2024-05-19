"""
Suppose we have three .pdf files in the directory ./temp
1_2.pdf, 3_4_5.pdf, and 6_7_7.pdf
and we want to merge them in a sequential manner into a single file
The merged document will be in the directory of ./temp/final.pdf

https://caendkoelsch.wordpress.com/2019/05/10/merging-multiple-pdfs-into-a-single-pdf/
"""

import PyPDF2

# Open the files that have to be merged one by one
pdf1_2   = open("./temp/1_2.pdf",   'rb')
pdf3_4_5 = open("./temp/3_4_5.pdf", 'rb')
pdf6_7_8 = open("./temp/6_7_8.pdf", 'rb')

# Instantiate pdf reader objects
pdf1_2_Reader = PyPDF2.PdfFileReader(pdf1_2)
pdf3_5_Reader = PyPDF2.PdfFileReader(pdf3_4_5)
pdf6_8_Reader = PyPDF2.PdfFileReader(pdf6_7_8)

# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the pagenumbers for the first document
for pageNum in range(pdf1_2_Reader.numPages):
    pageObj = pdf1_2_Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Loop through all the pagenumbers for the second document
for pageNum in range(pdf3_5_Reader.numPages):
    pageObj = pdf3_5_Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Loop through all the pagenumbers for the second document
for pageNum in range(pdf6_8_Reader.numPages):
    pageObj = pdf6_8_Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Now that all the pages have been copied 
# Write them into the a new document
pdfOutputFile = open('./temp/final.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
 
# Close all the files - Created as well as opened
pdfOutputFile.close()
pdf1_2.close()
pdf3_4_5.close()
pdf6_7_8.close()