from PyPDF2 import PdfFileMerger
from pathlib import Path

pdf_files =["./ToBeMerged/"+k.name for k in Path("./ToBeMerged/").rglob('*.pdf')] #pdf files in the current directory is stored in a list.

merger = PdfFileMerger()

for pdf in pdf_files:
    merger.append(pdf)

merger.write("./merged.pdf")
merger.close()
print("Merge completed")