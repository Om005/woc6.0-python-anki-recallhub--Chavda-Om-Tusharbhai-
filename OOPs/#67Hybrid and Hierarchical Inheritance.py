# #Hybrid inheritence
# class base:
#     pass
# class derived1(base):
#     pass
# class derived2(base):
#     pass
# class derived3(derived1, derived2):
#     pass

# # Hirerchical inheritence
# class base:
#     pass
# class derived1(base):
#     pass
# class derived2(base):
#     pass
# class derived3(base):
#     pass

import os
from PyPDF2 import PdfMerger

pdfs = os.listdir("data/make directory/Tutorial-2")
ok = PdfMerger()

for pdf in pdfs:
    ok.append(open(f"data/make directory/Tutorial-2/{pdf}", 'rb'))

ok.write("data/make directory/Tutorial-2/result1.pdf")
ok.close()