FROM python:3.10-slim

# Arbeitsverzeichnis im Container setzen
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere deinen Code ins Arbeitsverzeichnis des Containers
ARG SCRIPT_NAME=save_discover_weekly.py

COPY ./${SCRIPT_NAME} ./${SCRIPT_NAME}

CMD ["python", "./app.py"]