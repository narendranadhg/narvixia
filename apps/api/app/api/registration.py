from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File

from app.schemas.registration import Registration
from app.services.registration_service import process_registration
from app.core.services import services

router = APIRouter(
    prefix="/registration",
    tags=["Registration"]
)


@router.post("/")
def create_registration(registration: Registration):
    return process_registration(registration)


@router.post("/extract")
async def extract(file: UploadFile = File(...)):
    upload_dir = Path("app/uploads")
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = services.ocr.extract_text(str(file_path))

    return {
        "success": True,
        "filename": file.filename,
        "text": extracted_text
    }