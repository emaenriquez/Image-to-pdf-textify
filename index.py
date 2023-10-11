from reportlab.lib.pagesizes import letter
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Image

def image_to_pdf(image_path, pdf_path):
    # Crear un objeto PDF
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    
    # Cargar la imagen
    img = utils.ImageReader(image_path)
    img_width, img_height = img.getSize()
    
    # Ajustar el tamaño de la imagen para que se ajuste a la página
    aspect_ratio = img_width / img_height
    img_width = letter[0]
    img_height = letter[0] / aspect_ratio
    
    # Crear un objeto de imagen y agregarlo al documento PDF
    image = Image(image_path, width=img_width, height=img_height)
    story = [image]
    
    doc.build(story)

# Ruta de la imagen de entrada y ruta del archivo PDF de salida
image_path = 'tu_imagen.jpg'
pdf_path = 'imagen_a_pdf.pdf'

# Llamar a la función para convertir la imagen a PDF
image_to_pdf(image_path, pdf_path)
