from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class Patient(Base):
    """
    Korak 1: jedan jednostavan model da provjerimo da cela infrastruktura radi
    (FastAPI <-> SQLAlchemy <-> Postgres <-> Docker Compose).

    Doctor i Appointment dolaze u Koraku 1.5, kad ovo prvo proradi end-to-end.
    """

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False)
    phone = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True, unique=True, index=True)
    notes = Column(String(1000), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Back-reference: patient.appointments -> lista svih termina ovog pacijenta
    appointments = relationship("Appointment", back_populates="patient")
