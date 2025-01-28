from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import utils


POPPLER_PATH = r"C:\Release-24.08.0-0\poppler-24.08.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract(file_path,file_format):
    # extracting text from pdf
    pages = convert_from_path(file_path,poppler_path=POPPLER_PATH)
    document_txt = ""
    for page in pages:
        processed_image = utils.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image,lang='eng')
        document_txt = "\n" + text
        
    return document_txt
        
        
    # if file_format == "prescription":
    #     pass # extract data from prescrition
    # elif file_format == "patient_details":
    #     pass # extract data from patient details


if __name__ == "__main__":
    data = extract("../resources/patient_details/pd_1.pdf","prescription")
    print(data)