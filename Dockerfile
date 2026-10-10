
FROM python:3.12-slim

WORKDIR /app

COPY health_check.py .
COPY metrics_exporter.py .

RUN pip install --no-cache-dir psutil prometheus-client

EXPOSE 8000

CMD ["python", "metrics_exporter.py"]
