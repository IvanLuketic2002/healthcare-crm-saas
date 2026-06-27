from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


class PatientBase(BaseModel):
    full_name: str
    date_of_birth: date
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    notes: Optional[str] = None


class PatientCreate(PatientBase):
    """Sema za kreiranje novog pacijenta (POST request body)."""
    pass


class PatientUpdate(BaseModel):
    """Sema za delimicni update (PATCH) - sva polja opciona."""
    full_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    notes: Optional[str] = None


class PatientOut(PatientBase):
    """Sema za odgovor klijentu - dodaje polja koja baza generise."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
