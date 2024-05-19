import os
from PyPDF2 import PdfFileMerger

# pass the path of the parent_folder
def fetch_all_files(parent_folder: str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            target_files.append(os.path.join(path, name))
    return target_files 

# pass the path of the output final file.pdf and the list of paths
def merge_pdf(out_path: str, extracted_files: list [str]):
    merger = PdfFileMerger()
    
    for pdf in extracted_files:
        merger.append(pdf)

    merger.write(out_path)
    merger.close()

# get a list of all the paths of the pdf
parent_folder_path = './temp'
output_pdf_path    = './final.pdf'

extracted_files = fetch_all_files(parent_folder_path)
merge_pdf(output_pdf_path, extracted_files)