from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class Doctor(Base):
    """Lekar - jedan lekar moze imati vise termina (Appointment)."""

    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False, index=True)
    specialization = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True, unique=True, index=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Back-reference: doctor.appointments -> lista svih termina ovog lekara
    appointments = relationship("Appointment", back_populates="doctor")
