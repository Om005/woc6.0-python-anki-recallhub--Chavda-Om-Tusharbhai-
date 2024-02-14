# from PyPDF2 import PdfMerger

# pdfs = []
# for i in range (1,7):
#     pdfs.append(f"data/make directory/Tutorial-2/{i}.pdf")

# merger = PdfMerger()
# for pdf in pdfs:
#     merger.append(open(pdf, 'rb'))

# merger.write("data/make directory/Tutorial-2/result.pdf")
# merger.close()

import os
from PyPDF2 import PdfMerger

pdfs = os.listdir("data/make directory/Tutorial-2")
merger = PdfMerger()

for pdf in pdfs:
    merger.append(open(f"data/make directory/Tutorial-2/{pdf}", 'rb'))

merger.write("data/make directory/Tutorial-2/hm.pdf")
merger.close()