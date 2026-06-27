from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


class DoctorBase(BaseModel):
    full_name: str
    specialization: str
    email: Optional[EmailStr] = None


class DoctorCreate(DoctorBase):
    """Sema za kreiranje novog lekara (POST request body)."""
    pass


class DoctorUpdate(BaseModel):
    """Sema za delimicni update (PATCH) - sva polja opciona."""
    full_name: Optional[str] = None
    specialization: Optional[str] = None
    email: Optional[EmailStr] = None


class DoctorOut(DoctorBase):
    """Sema za odgovor klijentu - dodaje polja koja baza generise."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
