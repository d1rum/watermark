import PyPDF4
from PyPDF4 import PdfFileReader,PdfFileWriter
from reportlab.pdfgen import canvas
from io import BytesIO
imgTemp = BytesIO()
imgDoc = canvas.Canvas(imgTemp)
imgPath = "logo4.png"
imgDoc.drawImage(imgPath, 399, 700, 150, 75)    
imgDoc.save()
def watermark(input_pdf,output_pdf):
    watermark = PdfFileReader(BytesIO(imgTemp.getvalue()))
    page_watermark = watermark.getPage(0)
    input_pdf_reader  = PdfFileReader(input_pdf)
    output_pdf_writer = PdfFileWriter()
    for page in range(input_pdf_reader.getNumPages()):
        page  = input_pdf_reader.getPage(page)
        firstpage = input_pdf_reader.getPage(0)
        firstpage.mergePage(page_watermark)
        output_pdf_writer.addPage(page)
    with open(output_pdf,"wb") as output:
        output_pdf_writer.write(output)              
if __name__ == "__main__":
    watermark(input_pdf="pdf.pdf",output_pdf="output.pdf")
