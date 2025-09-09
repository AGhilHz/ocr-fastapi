# OCR FastAPI Service with PaddleOCR

[🇮🇷 راهنمای فارسی](./README.fa.md)

This project provides a **FastAPI-based OCR (Optical Character Recognition) service**  
using [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR).

---

## Features
- 🚀 REST API for OCR via FastAPI
- 🔑 Secure with API key header
- 🖼 Works with remote image URLs
- ✅ Tested with PaddleOCR v3.2 and Python 3.10

---

## Installation and Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/AGhilHz/ocr-fastapi.git
   cd ocr-fastapi
   ```

2. **Create a virtual environment**

   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Service

### Method 1: Run directly with uvicorn

```bash
uvicorn ocr_fast:app --host 0.0.0.0 --port 8090
```

### Method 2: Run permanently with systemd

1. Create the service file:

   ```bash
   sudo nano /etc/systemd/system/ocr-fast.service
   ```

   Content:

   ```
   [Unit]
   Description=OCR FastAPI Service
   After=network.target

   [Service]
   User=root
   WorkingDirectory=/var/www/ocr-fast
   ExecStart=/var/www/ocr-fast/.venv/bin/uvicorn ocr_fast:app --host 0.0.0.0 --port 8090
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. Enable and start the service:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable ocr-fast
   sudo systemctl start ocr-fast
   ```

3. Check the service status:

   ```bash
   systemctl status ocr-fast
   ```

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
```

---

## Notes

- 🔑 Change the `API_KEY` value in the code (`ocr_fast.py`).
- ⚡ You can modify the port and path by editing the `ExecStart` line in the systemd service file.

---

## About

FastAPI + PaddleOCR service for OCR with preprocessing