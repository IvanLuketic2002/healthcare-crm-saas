# Lagana Python slika - bitno za Free Tier (manje resursa, brzi build)
FROM python:3.12-slim

WORKDIR /code

# Prvo zavisnosti (iskoristi Docker layer cache - brzi rebuild kad samo kod promenis)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Onda kod aplikacije
COPY ./app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
