# ---- imagem base -----------------------------------------------------------
    FROM python:3.12-slim

    # ---- variáveis de ambiente -------------------------------------------------
    ENV PYTHONDONTWRITEBYTECODE=1 \
        PYTHONUNBUFFERED=1 \
        DJANGO_SETTINGS_MODULE=techcommerce.settings \
        POETRY_VERSION=1.8.2
    
    # ---- sistema & dependências ------------------------------------------------
    RUN apt-get update && apt-get install -y --no-install-recommends \
            build-essential libpq-dev gcc && \
        pip install --no-cache-dir "poetry==$POETRY_VERSION" && \
        apt-get purge -y build-essential && apt-get autoremove -y && \
        rm -rf /var/lib/apt/lists/*
    
    # ---- diretórios ------------------------------------------------------------
    WORKDIR /app
    COPY pyproject.toml poetry.lock* /app/
    
    # ---- instalar libs Python --------------------------------------------------
    RUN poetry config virtualenvs.create false && \
        poetry install --no-interaction --no-ansi --only main
    
    # ---- copiar código ---------------------------------------------------------
    COPY . /app
    
    # ---- comando default -------------------------------------------------------
    CMD ["gunicorn", "techcommerce.asgi:application", "-b", "0.0.0.0:8000"]
    