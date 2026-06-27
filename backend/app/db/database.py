import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ceo connection string dolazi iz environment varijable.
# U docker-compose.yml definisacemo je tako da pokazuje na "db" servis (ime kontejnera).
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/healthcare_crm",
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency za FastAPI - otvara sesiju, vraca je nakon zavrsetka requesta."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
