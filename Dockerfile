FROM python:3.12-slim

WORKDIR /app

COPY health_check.py .

RUN pip install --no-cache-dir psutil

CMD ["python", "health_check.py"]