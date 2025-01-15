from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
import os
import uuid
from models.whisper_model import transcribe_audio
from models.llm_model import generate_report, create_pdf_from_html
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

database = """
Date: 11/11/2024
Area Assessed: Interior Hallway
Location: 4248 Windsor Street
Assessor: Trung Jr
"""

# Serve the HTML interface
@app.get("/", response_class=HTMLResponse)
async def get_html():
    with open("templates/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

# Transcription route
@app.post("/report-generate")
async def transcribe_audios(file: UploadFile = File(...), language: str = "English"):
    unique_code = uuid.uuid4()
    os.makedirs("audios", exist_ok=True)
    os.makedirs("texts", exist_ok=True)

    file_name = file.filename.split(".")[0]
    audio_data = await file.read()
    unique_filename = f"audios/{unique_code}_{file_name}.mp3"
    with open(unique_filename, "wb") as f:
        f.write(audio_data)

    text_result = await transcribe_audio(unique_filename)
    transcription_filename = f"texts/{unique_code}_{file_name}.txt"
    with open(transcription_filename, "w", encoding="utf-8") as f:
        f.write(text_result)
    os.remove(unique_filename)
    os.remove(transcription_filename)
    
    report_html = await generate_report(transcription_filename, database=database, language=language)
    report_pdf = create_pdf_from_html(report_html)
    return StreamingResponse(report_pdf, media_type="application/pdf", headers={"Content-Disposition": "inline; filename=report.pdf"})

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)