FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/usr/local/bin:$PATH"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pytest pytest-cov

COPY pyproject.toml /app/

COPY . /app

CMD ["gunicorn", "techcommerce.wsgi:application", "-b", "0.0.0.0:8000"] 