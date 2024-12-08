'''
#Install PyPDF2 	
pip install PyPDF2
#Install ReportLab
pip install reportlab
'''


import os
from PyPDF2 import PdfMerger

# Specify the directory containing the PDF files
pdf_dir = "E:\pdf\LULC_Map"

# Create a PdfMerger object
merger = PdfMerger()

# Loop through all the files in the directory
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        #print(filename)        
        file_path = os.path.join(pdf_dir, filename)
        merger.append(file_path)
        #print(file_path)

# Create the full path for the PDF file
output_file = os.path.join(pdf_dir, "Merge.pdf")

# Output the merged PDF to a file
with open(output_file, "wb") as output_pdf:
    merger.write(output_pdf)

# Close the PdfMerger object
merger.close()

print(f"All PDFs have been merged into {output_file}")
