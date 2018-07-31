from fpdf import FPDF
pdf = FPDF()
# imagelist is the list with all image filenames
imagelist = ['Samples/test.jpg', 'Samples/Edged.jpg', 'Samples/transformed.png']
for image in imagelist:
    pdf.add_page()
    pdf.image(image, 5, 5, 200, 200)
pdf.output("Samples/Output.pdf", "F")
