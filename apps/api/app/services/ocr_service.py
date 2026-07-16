from pathlib import Path
import easyocr


class OCRService:
    """
    OCR Service using EasyOCR.

    Responsibilities:
    - Load OCR model once
    - Extract text from supported documents
    """

    def __init__(self):
        print("Loading EasyOCR model...")

        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

        print("EasyOCR model loaded successfully.")

    def extract_text(self, file_path: str) -> str:
        """
        Extract text from a document.

        Args:
            file_path: Path to the document.

        Returns:
            Extracted text.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        results = self.reader.readtext(
            str(path),
            detail=0
        )

        return "\n".join(results).strip()