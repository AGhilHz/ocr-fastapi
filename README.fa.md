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