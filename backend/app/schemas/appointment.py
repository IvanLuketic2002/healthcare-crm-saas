from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.appointment import AppointmentStatus


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    scheduled_at: datetime
    status: AppointmentStatus = AppointmentStatus.SCHEDULED
    reason: Optional[str] = None


class AppointmentCreate(AppointmentBase):
    """Sema za kreiranje novog termina (POST request body)."""
    pass


class AppointmentUpdate(BaseModel):
    """Sema za delimicni update (PATCH) - sva polja opciona."""
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    scheduled_at: Optional[datetime] = None
    status: Optional[AppointmentStatus] = None
    reason: Optional[str] = None


class AppointmentOut(AppointmentBase):
    """Sema za odgovor klijentu - dodaje polja koja baza generise."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
