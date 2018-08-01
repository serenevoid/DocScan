from fpdf import FPDF

def pdf(list):
	pdf = FPDF()
	# imagelist is the list with all image filenames
	imagelist = list
	for image in imagelist:
	    pdf.add_page()
	    pdf.image("Thresholded/{}".format(image), 5, 5, 200, 200)
	pdf.output("PDF/Output.pdf", "F")

