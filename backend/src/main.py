from fastapi import FastAPI,Form,UploadFile,File
import uvicorn
from extractor import extract

app = FastAPI() 

@app.post("/extract_from_doc")
def extract_from_doc(file_format: str = Form(...),
                     file: UploadFile = File(...)):
    content = file.file.read()
    
    with open("uploads/test.pdf",'wb') as f:
        f.write(content)

if __name__ == '__main__':
    uvicorn.run(app,host="localhost",port=8000)