#!/usr/bin/python3
import glob
import os
import qrcode
import module

pdfM = module.pdfTools()

extensions = (".pdf", ".PDF")

input_path = "inputFiles"
output_path = "outputFiles"
Files = sum(
        [glob.glob(os.path.join(input_path, "*" + x))
         for x in extensions],
        [])

for File in Files:
    print(File)
    #  get page number
    page = pdfM.getPageNumber(File)

    # create of QRCode of the page number
    pdfM.createQRCode(page)

    # add image to pdf
    pdfM.addImage(File,output_path)
    


