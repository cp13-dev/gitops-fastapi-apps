# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
