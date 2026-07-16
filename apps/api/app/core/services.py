from app.services.ocr_service import OCRService


class Services:
    def __init__(self):
        print("Initializing application services...")
        self.ocr = OCRService()
        print("Application services initialized.")


services = Services()