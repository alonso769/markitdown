import os
import zipfile
import pytesseract
from PIL import Image
from io import BytesIO
from markitdown import MarkItDown
import fitz  # PyMuPDF

# Ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_imagen_bytes(bytes_imagen):
    try:
        imagen = Image.open(BytesIO(bytes_imagen))
        return pytesseract.image_to_string(imagen, lang='spa')
    except Exception:
        return ""

def ocr_imagen(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    return pytesseract.image_to_string(imagen, lang='spa')

def procesar_pdf(ruta_pdf):
    md = MarkItDown()
    texto_final = md.convert(ruta_pdf).text_content

    doc = fitz.open(ruta_pdf)
    texto_imagenes = ""
    for num_pagina in range(len(doc)):
        for idx, img in enumerate(doc[num_pagina].get_images(full=True)):
            xref = img[0]
            base_imagen = doc.extract_image(xref)
            texto_ocr = ocr_imagen_bytes(base_imagen["image"])
            if texto_ocr.strip():
                texto_imagenes += f"\n\n--- Texto de imagen (página {num_pagina+1}) ---\n{texto_ocr}"
    doc.close()

    if texto_imagenes:
        texto_final += "\n\n## Texto extraído de imágenes dentro del PDF\n" + texto_imagenes

    return texto_final

def procesar_office(ruta_archivo):
    """Funciona para .pptx y .docx, ya que ambos son ZIP con carpeta 'media'."""
    md = MarkItDown()
    texto_final = md.convert(ruta_archivo).text_content

    texto_imagenes = ""
    try:
        with zipfile.ZipFile(ruta_archivo, 'r') as z:
            archivos_media = [n for n in z.namelist() if '/media/' in n and n.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
            for nombre in archivos_media:
                bytes_imagen = z.read(nombre)
                texto_ocr = ocr_imagen_bytes(bytes_imagen)
                if texto_ocr.strip():
                    texto_imagenes += f"\n\n--- Texto de imagen ({os.path.basename(nombre)}) ---\n{texto_ocr}"
    except Exception as e:
        print(f"Aviso: no se pudieron leer imágenes internas ({e})")

    if texto_imagenes:
        texto_final += "\n\n## Texto extraído de imágenes dentro del archivo\n" + texto_imagenes

    return texto_final

def procesar_archivo(ruta):
    ext = os.path.splitext(ruta)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
        return ocr_imagen(ruta)
    elif ext == '.pdf':
        return procesar_pdf(ruta)
    elif ext in ['.pptx', '.docx']:
        return procesar_office(ruta)
    else:
        return MarkItDown().convert(ruta).text_content

if __name__ == "__main__":
    ruta_archivo = input("Pega la ruta del archivo (PDF, PPTX, DOCX o imagen): ").strip('"')
    texto = procesar_archivo(ruta_archivo)
    with open("resultado_completo.md", "w", encoding="utf-8") as f:
        f.write(texto)
    print("Listo, revisa resultado_completo.md")