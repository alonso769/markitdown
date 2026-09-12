import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

imagen = Image.open(r"C:\Users\Alonso\Desktop\tuimagen.jpg")

texto = pytesseract.image_to_string(imagen, lang='spa')

with open("resultado_imagen.md", "w", encoding="utf-8") as f:
    f.write(texto)

print("Listo, revisa resultado_imagen.md")