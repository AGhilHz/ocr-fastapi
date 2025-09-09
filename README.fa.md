# سرویس OCR مبتنی بر FastAPI با PaddleOCR

[🇬🇧 English Guide](./README.md)

این پروژه یک **سرویس OCR (تشخیص نوری کاراکتر) مبتنی بر FastAPI**  
را با استفاده از [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) فراهم می‌کند.

---

## ویژگی‌ها
- 🚀 REST API برای OCR از طریق FastAPI
- 🔑 ایمن با هدر کلید API
- 🖼 کار با URLهای تصاویر راه دور
- ✅ تست شده با PaddleOCR نسخه 3.2 و Python 3.10

---

## نصب و راه‌اندازی

1. **کلون مخزن**

   ```bash
   git clone https://github.com/AGhilHz/ocr-fastapi.git
   cd ocr-fastapi
   ```

2. **ساخت محیط مجازی**

   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate
   ```

3. **نصب وابستگی‌ها**

   ```bash
   pip install -r requirements.txt
   ```

---

## اجرای سرویس

### روش ۱: اجرای مستقیم با uvicorn

```bash
uvicorn ocr_fast:app --host 0.0.0.0 --port 8090
```

### روش ۲: اجرای دائمی با systemd

1. فایل سرویس را ایجاد کنید:

   ```bash
   sudo nano /etc/systemd/system/ocr-fast.service
   ```

   محتوا:

   ```
   [Unit]
   Description=سرویس OCR مبتنی بر FastAPI
   After=network.target

   [Service]
   User=root
   WorkingDirectory=/var/www/ocr-fast
   ExecStart=/var/www/ocr-fast/.venv/bin/uvicorn ocr_fast:app --host 0.0.0.0 --port 8090
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. فعال‌سازی و اجرای سرویس:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable ocr-fast
   sudo systemctl start ocr-fast
   ```

3. بررسی وضعیت سرویس:

   ```bash
   systemctl status ocr-fast
   ```

---

## مثال

تصویر ورودی:  
![نمونه OCR](https://upload.wikimedia.org/wikipedia/commons/5/57/Lorem_Ipsum_Helvetica.png)

درخواست:

```bash
curl -X POST http://سرور-شما:8090/ocr-fast \
  -H "x-api-key: test-api-key-1234" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Lorem_Ipsum_Helvetica.png"}'
```

---

## نکات

- 🔑 مقدار `API_KEY` را در کد (`ocr_fast.py`) تغییر دهید.
- ⚡ می‌توانید با ویرایش خط `ExecStart` در فایل سرویس systemd، پورت و مسیر را تغییر دهید.

---

## درباره

سرویس FastAPI + PaddleOCR برای OCR با پیش‌پردازش