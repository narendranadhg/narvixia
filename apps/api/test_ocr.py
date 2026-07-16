from app.services.ocr_service import OCRService

ocr = OCRService()

text = ocr.extract_text("sample_aadhaar.jpg")

print(text)