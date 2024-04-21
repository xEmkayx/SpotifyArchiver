FROM python:3.10

# Arbeitsverzeichnis im Container setzen
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8123

CMD ["python", "./webserver.py"]