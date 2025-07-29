import PyPDF2
# we are opening file 
with open (r"C:\Users\ashis\OneDrive\Desktop\Data Automation\pdf_automation\split_pdf\merger_output.pdf","rb") as file:
    reader=PyPDF2.PdfReader(file)
    writer=PyPDF2.PdfWriter()
    # for loop to rotate the page 
    for i, pages in enumerate (reader.pages):
            rotated_pages=pages.rotate(90)   # we can only rotate 90*, 180*, 270 and to rectify use (negetive value -90 etc..)
            writer.add_page(rotated_pages)
with open ("rotate_output.pdf","wb") as output:
    writer.write(output)