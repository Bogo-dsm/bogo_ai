from fastapi import FastAPI, Form, UploadFile, File, HTTPException, Body, Header
import uvicorn
import io
import pdfplumber
import httpx
import os
from dotenv import load_dotenv
load_dotenv()
VALID_API_KEY = os.getenv("X_API_KEY")
from .summarizer import pdf_load, summarize

app = FastAPI()


@app.post("/upload")
async def upload_file(  # 파일 읽기는 비동기(async) 권장
    x_api_key: str = Header(...),
    name: str = Form(...),
    file: UploadFile = File(...)
):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    content = await file.read()

    with pdfplumber.open(io.BytesIO(content)) as pdf:
        full_text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"

    re_text = pdf_load(full_text)
    summarized_text = summarize(re_text)
    payload = {
        "name": name,
        "description": summarized_text["desc"],
        "tone": summarized_text["tone"],
        "character":summarized_text["character"]
    }

    async with httpx.AsyncClient() as client:
        try:
            headers = {"X-API-KEY": VALID_API_KEY}
            # 전체 URL을 사용하세요!
            external_response = await client.post("http://127.0.0.1:8000/create", json=payload, headers=headers)

            # 200번대 응답이 아니면 예외 발생
            external_response.raise_for_status()

            return {"status": "success", "detail": "Data sent successfully"}

        except httpx.HTTPStatusError as e:
            # 외부 서버 응답 에러 (예: 404, 500)
            raise HTTPException(status_code=e.response.status_code, detail="External server error")
        except Exception as e:
            # 연결 실패 등 기타 에러
            raise HTTPException(status_code=500, detail=f"Connection failed: {str(e)}")

@app.post("/create")
def sdf(
    x_api_key: str = Header(...),
    name: str = Body(...),
    description: str = Body(...),
    tone: str = Body(...),
    character: str = Body(...)
):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    return {"wow":"지리네"}

if __name__ == "__main__":
    uvicorn.run(app)