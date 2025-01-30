from fastapi import FastAPI,Form,UploadFile,File
import uvicorn
from backend.src.extractor import extract
import os
import uuid


app = FastAPI() 

@app.post("/extract_from_doc")
async def extract_from_doc(file_format: str = Form(...), file: UploadFile = File(...)):
    print(f"Received file format: {file_format}")
    print(f"Received file name: {file.filename}")

    # Define upload directory path
    upload_dir = os.path.join("backend", "uploads")
    os.makedirs(upload_dir, exist_ok=True)  #  Ensure directory exists

    # file_path = os.path.join(upload_dir, file.filename)
    file_path = os.path.join(upload_dir, (str(uuid.uuid4())+".pdf"))
    
    with open(file_path, "wb") as f:
        f.write(await file.read())  # Save uploaded file

    print(f"File saved successfully at: {file_path}")
    
    # Call extract function
    try:
        extracted_data = extract(file_path, file_format)
    except Exception as e:
        extracted_data = {'error':str(e)}
    if os.path.exists(file_path):
        os.remove(file_path)
    return {"extracted_data": extracted_data}


if __name__ == '__main__':
    uvicorn.run(app,host="localhost",port=8000)