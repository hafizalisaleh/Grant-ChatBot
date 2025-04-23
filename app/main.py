from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse
from .document_processor import process_document

app = FastAPI(title="Grant Chatbot API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
async def generate(prompt: str = Form(...), doc: UploadFile = File(...)):
    """
    Receive a prompt & a .docx, return an updated .docx
    """
    new_doc_bytes = await process_document(doc, prompt)
    return StreamingResponse(
        iter([new_doc_bytes]),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": "attachment; filename=updated.docx"}
    )
