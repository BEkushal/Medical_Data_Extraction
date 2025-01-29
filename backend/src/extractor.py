from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import backend.src.utils as utils
from backend.src.parser_prescription import PrescriptionParser
from backend.src.parser_patient_details import PatientDetailsParser


POPPLER_PATH = r"C:\Release-24.08.0-0\poppler-24.08.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract(file_path,file_format):
    # extracting text from pdf
    pages = convert_from_path(file_path,poppler_path=POPPLER_PATH)
    document_txt = ""
    if len(pages)>0:
        page = pages[0]
        processed_image = utils.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image,lang='eng')
        document_txt = "\n" + text
    
        
        
    # Select fields from text 
    if file_format == "prescription":
        extracted_data = PrescriptionParser(document_txt).parse() # extract data from prescrition
    elif file_format == "patient_details":
        extracted_data = PatientDetailsParser(document_txt).parse() # extract data from patient details
    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data

if __name__ == "__main__":
    data = extract("../resources/prescription/pre_2.pdf","prescription")
    print(data)