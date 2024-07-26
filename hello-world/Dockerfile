FROM python:3.10.11-slim

COPY . /app

WORKDIR /app

EXPOSE 8000

ENV BASIC_AUTH_USERNAME=admin
ENV BASIC_AUTH_PASSWORD=secretpassword

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]