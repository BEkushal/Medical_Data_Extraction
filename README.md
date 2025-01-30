# Medical Data Extraction

## Project Overview

This project is a **medical report data extraction system** that processes images of medical reports and extracts important details. The application uses **computer vision, OCR (Optical Character Recognition), and regular expressions** to extract:

- Patient details (Name, Address, Phone Number, Medical Problems, etc.)
- Prescription details (Medicines, Dosage Instructions, Refill Information, etc.)

The backend is built using **FastAPI**, and **Postman** is used as the frontend for API testing.

---

## Project Architecture

The application follows a **simplified three-tier architecture**:

1. **Frontend**: Postman (for API interaction and testing)
2. **Backend**: FastAPI (Handles file uploads, processing, and data extraction)
3. **Testing**: Pytest (Unit tests for parsers)

---

## Installation Guide

### Prerequisites

Ensure you have **Python 3.8+** installed on your system. Also, install **Tesseract OCR** and **Poppler**:

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/)

### Steps to Set Up

1. Clone the repository:
   ```sh
   git clone https://github.com/BEkushal/Medical-Data-Extraction.git
   cd medical-data-extraction
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the FastAPI server:
   ```sh
   uvicorn backend.src.main:app --reload
   ```

---

## API Endpoints

### 1. Extract Data from a Medical Document

**Endpoint:** `POST /extract_from_doc`

**Description:** Accepts a **PDF file** of a medical report and extracts relevant data.

**Request Parameters:**

- `file_format` (Form data) – Specify the document type (`prescription` or `patient_details`)
- `file` (File Upload) – Medical report (PDF)

**Example Request (using Postman or cURL):**

```sh
curl -X 'POST' \
  'http://localhost:8000/extract_from_doc' \
  -F 'file_format=prescription' \
  -F 'file=@/path/to/medical_report.pdf'
```

**Example Response:**

```json
{
    "extracted_data": {
        "patient name": "John Doe",
        "patient address": "123 Main St, NY",
        "medicines": "Paracetamol 500mg",
        "directions": "Take one tablet every 8 hours",
        "refill": "2 times"
    }
}
```


## Key Dependencies

```
pdf2image
pytesseract
opencv-python
numpy
pandas
Pillow
fastapi
pytest
uvicorn
python-multipart
```

---

## How It Works

### 1. Image Preprocessing (`utils.py`)

- Converts the image to grayscale
- Applies adaptive thresholding for better OCR results

### 2. Text Extraction (`extractor.py`)

- Uses `pytesseract` to extract text from the preprocessed image
- Selects relevant fields based on the document type (`prescription` or `patient_details`)

### 3. Parsing (`parser_prescription.py`, `parser_patient_details.py`)

- Uses regex to extract structured information from the OCR text

---

## Running Tests

To run unit tests:

```sh
pytest tests/
```

---

## Future Enhancements

✅ Add support for scanned images (JPG, PNG) ✅ Improve regex for better accuracy ✅ Implement a frontend for better user experience

---

## License

This project is licensed under the MIT License.

---

## Contributors

- Kushalappa BE ([kushalappa193@gmail.com](mailto\:kushalappa193@gmail.com))

---

### ⭐ If you like this project, consider giving it a star on GitHub! ⭐