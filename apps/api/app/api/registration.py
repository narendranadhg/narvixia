from pathlib import Path
import shutil
from uuid import uuid4

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.schemas.registration import Registration
from app.services.registration_service import process_registration
from app.core.services import services
from app.core.config import settings

router = APIRouter(
    prefix="/registration",
    tags=["Registration"],
)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf"}


@router.post("/")
def create_registration(registration: Registration):
    return process_registration(registration)


@router.post("/extract")
async def extract(file: UploadFile = File(...)):
    try:
        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="Filename is required."
            )

        extension = Path(file.filename).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type. Only JPG, JPEG, PNG and PDF are allowed."
            )

        upload_dir = Path(settings.UPLOAD_FOLDER)
        upload_dir.mkdir(parents=True, exist_ok=True)

        unique_filename = f"{uuid4()}{extension}"
        file_path = upload_dir / unique_filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = services.ocr.extract_text(str(file_path))

        return {
            "success": True,
            "original_filename": file.filename,
            "stored_filename": unique_filename,
            "text": extracted_text,
        }

    except HTTPException:
        raise

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process document: {str(ex)}"
        )