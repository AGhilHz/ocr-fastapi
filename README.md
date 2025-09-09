# OCR FastAPI Service with PaddleOCR

[🇮🇷  راهنمای فارسی](./README.fa.md)

This project provides a **FastAPI-based OCR (Optical Character Recognition) service**  
using [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR).

---

## Features
- 🚀 REST API for OCR via FastAPI
- 🔑 Secure with API key header
- 🖼 Works with remote image URLs
- ✅ Tested with PaddleOCR v3.2 and Python 3.10

---

## Example

Input image:  
![OCR Sample](https://upload.wikimedia.org/wikipedia/commons/5/57/Lorem_Ipsum_Helvetica.png)

Request:
```bash
curl -X POST http://your-server:8090/ocr-fast \
  -H "x-api-key: test-api-key-1234" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Lorem_Ipsum_Helvetica.png"}'
