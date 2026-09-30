# Stage 1: Abhängigkeiten in eine venv installieren
FROM python:3.14-slim AS builder
COPY requirements.txt .
RUN python -m venv /opt/venv && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Laufzeit-Image, übernimmt nur die fertige venv und den Code
FROM python:3.14-slim

# print() sofort ausgeben, damit es in "docker compose logs" erscheint
ENV PYTHONUNBUFFERED=1
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY src/ .
