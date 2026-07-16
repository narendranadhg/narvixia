from pydantic import BaseModel, EmailStr


class Registration(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    dob: str | None = None
    gender: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    address: str | None = None

class RegistrationRequest(BaseModel):
    text: str