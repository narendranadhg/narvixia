from app.schemas.registration import Registration


def process_registration(registration: Registration):
    return {
        "success": True,
        "message": "Registration processed successfully.",
        "data": registration
    }