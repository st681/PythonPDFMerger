import os
from PyPDF2 import PdfReader, PdfMerger

def merge_pdfs_in_current_folder():
    folder_path = os.getcwd()
    merger = PdfMerger()
    files = sorted(os.listdir(folder_path))

    for file in files:
        if file.endswith('.pdf'):
            with open(os.path.join(folder_path, file), 'rb') as f:
                pdf = PdfReader(f)
                merger.append(pdf)

    output_filename = os.path.join(folder_path, 'merged_document.pdf')
    with open(output_filename, 'wb') as f:
        merger.write(f)
    
    print(f"Merged PDF saved as {output_filename}")

merge_pdfs_in_current_folder()
