# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip \
    && python -m pip install "fastapi[standard]" pydantic-settings

EXPOSE 8000

CMD ["uvicorn", "git_day_practice.api:app", "--host", "0.0.0.0", "--port", "8000"]
