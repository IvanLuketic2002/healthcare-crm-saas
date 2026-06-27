from fastapi import FastAPI

from app.db.database import Base, engine
from app.routers import patients, doctors, appointments

app = FastAPI(
    title="Healthcare CRM SaaS - MVP",
    description="Korak 1: jednostavan Patient CRUD da provjerimo da infrastruktura radi.",
    version="0.1.0",
)

# Pravi tabele ako ne postoje. Za pravu produkciju bismo koristili Alembic migracije,
# ali za Korak 1 MVP-a ovo je dovoljno - ne komplikujemo rano.
Base.metadata.create_all(bind=engine)

app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)


@app.get("/health")
def health_check():
    """Health check endpoint - kasnije ga koristi i Kubernetes liveness/readiness probe."""
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Healthcare CRM SaaS API - vidi /docs za Swagger UI"}
