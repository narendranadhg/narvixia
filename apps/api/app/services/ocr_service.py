from pathlib import Path
import easyocr


class OCRService:
    """
    Handles Optical Character Recognition (OCR)
    using EasyOCR.
    """

    def __init__(self):
        print("Loading EasyOCR model...")
        self.reader = easyocr.Reader(["en"])
        print("EasyOCR model loaded successfully.")

    def extract_text(self, file_path: str) -> str:
        """
        Extract text from an image.

        Args:
            file_path (str): Path to the image.

        Returns:
            str: Extracted text.
        """

        results = self.reader.readtext(file_path, detail=0)

        return "\n".join(results)