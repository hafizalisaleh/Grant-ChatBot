from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from .document_processor import process_document

app = FastAPI(title="Grant Chatbot API")

# 1️⃣ API routes
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
async def generate(prompt: str = Form(...), doc: UploadFile = File(...)):
    new_doc = await process_document(doc, prompt)
    return StreamingResponse(
        iter([new_doc]),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition":"attachment; filename=updated.docx"}
    )

# 2️⃣ Serve index.html at the root
@app.get("/", include_in_schema=False)
def serve_ui():
    return FileResponse("static/index.html")

# 3️⃣ Mount all the rest of your frontend assets under /static
app.mount("/static", StaticFiles(directory="static"), name="static")
