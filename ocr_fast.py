from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import httpx
import numpy as np
import cv2
from paddleocr import PaddleOCR
import uvicorn

# ⚠️ Use your own API key in production
API_KEY = "test-api-key-1234"

# ✅ PaddleOCR v3.2
ocr_fast = PaddleOCR(lang='en')

app = FastAPI()

class OCRRequest(BaseModel):
    url: str

async def fetch_image_bytes(url: str) -> bytes:
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(url, follow_redirects=True)
        r.raise_for_status()
        if "image" not in r.headers.get("Content-Type", ""):
            raise HTTPException(status_code=400, detail="URL is not an image")
        return r.content

def decode_to_mat(img_bytes: bytes) -> np.ndarray:
    arr = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Failed to decode image")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def preprocess_image(img: np.ndarray) -> np.ndarray:
    """
    Preprocessing to better detect small characters like %
    """
    # Upscale (2x)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Adaptive threshold for better contrast
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        35, 11
    )

    # Back to 3-channel RGB
    proc = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
    return proc

@app.post("/ocr-fast")
async def perform_ocr_fast(body: OCRRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")

    try:
        img_bytes = await fetch_image_bytes(body.url)
        img = decode_to_mat(img_bytes)

        # 🔥 Preprocess for higher accuracy
        proc_img = preprocess_image(img)

        result = ocr_fast.ocr(proc_img)
        lines = result[0] if result else []
        texts = [line[1][0] for line in lines]

        return {"success": True, "texts": texts}

    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run("ocr_fast:app", host="0.0.0.0", port=8090)
