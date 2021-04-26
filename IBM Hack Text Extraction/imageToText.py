from PIL import Image
import PIL.Image
from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR'
TESSDATA_PREFIX ='CC:\Program Files\Tesseract-OCR'
output = pytesseract.image_to_string(PIL.Image.open('image.png').convert("RGB"), lang='eng')
print (output)