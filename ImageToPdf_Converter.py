import img2pdf
from pathlib import Path

INPUT_PATH = "./ToBeConverted/"

with open("./converted.pdf", "wb") as f:
    f.write(img2pdf.convert([INPUT_PATH + i.name for i in Path(INPUT_PATH).rglob('*.jpg')]))
    print("conversion complete")

