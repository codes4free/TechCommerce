FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev gcc \
    && pip install --no-cache-dir "poetry==1.8.2" \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && apt-get purge -y build-essential gcc && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
COPY . /app
CMD ["gunicorn", "techcommerce.wsgi:application", "-b", "0.0.0.0:8000"]