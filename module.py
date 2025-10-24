#!/usr/bin/python3
#from PyPDF2 import PdfReader, PdfWriter, PdfMerger
#import shutil
import fitz # PyMuPDF
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode

class pdfTools():
    def __init__(self):
        self.temp=1

    def copy_pdf(self,input_path, output_path):
        shutil.copy(input_path, output_path)

    def addImage(self,File,outputPath):
        # Get the file name with extension
        file_name_with_ext = os.path.basename(File)

        # Open the existing PDF
        pdf_path = File
        output_path = outputPath + "/" + file_name_with_ext
        doc = fitz.open(pdf_path)
        
        # Choose the page number (0-based index)
        page = doc[0]  # first page
        
        # Define the image and where to place it
        image_path = "my_qrPY.png" #"example.jpg"  # Path to your image file
        size = 20
        startX = 550
        startY = 750
        endX = startX+size
        endY = startY+size
        rect = fitz.Rect(startX, startY, endX, endY)  # (x0, y0, x1, y1)
        
        # Insert the image
        page.insert_image(rect, filename=image_path)
        
        # Save to a new file
        doc.save(output_path)
        doc.close()
        
        print("✅ QRCode added successfully!")

    def createQRCode(self, Value):
        img = qrcode.make(Value)
        img.save("my_qrPY.png")


    def getPageNumber(self,File):
        # Open the PDF
        pdf_path = File
        doc = fitz.open(pdf_path)
        
        # Select a page (0-based index)
        page = doc[0]
        
        # Define your rectangle area (x0, y0, x1, y1)
        # coordinates are in points (1/72 inch), origin at top-left

        startX = 300-5
        startY = 750+5
        endX = startX+20
        endY = startY
        rect = fitz.Rect(startX, startY, endX, endY)
        
        # Extract text from that area
        PageNumber = page.get_text("text", clip=rect).strip() 
        #print( PageNumber )
        
        # Close document
        doc.close()

        return PageNumber

    
    def verifyQRCode(self, File, output_path):
        # get the name of the output file
        file_name_with_ext = os.path.basename(File)
        pdf_path = output_path + "/" + file_name_with_ext
        print(pdf_path)

        # Convert PDF pages to images
        pages = convert_from_path(pdf_path, dpi=300)
        results = []
    
        for page_number, page in enumerate(pages, start=1):
            # Convert page to image
            img = page.convert('RGB')
    
            # Decode QR codes in the image
            decoded_objects = decode(img)
    
            for obj in decoded_objects:
                data = obj.data.decode('utf-8')
                results.append({
                    'page': page_number,
                    'data': data,
                    'type': obj.type
                })
    
        return results
