FROM python:3.11-slim

# Install system binaries: Tesseract OCR, English language packs, OpenCV dependencies, libmagic
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-eng \
    libgl1 \
    libglib2.0-0 \
    libmagic1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application source
COPY . .

# Set container environment variables
ENV FLASK_ENV=production \
    PYTHONUNBUFFERED=1 \
    TESSERACT_CMD=/usr/bin/tesseract \
    PORT=5000

# Expose default port
EXPOSE 5000

# Create entrypoint shell command that ensures tables & seeds exist, then runs gunicorn
CMD ["sh", "-c", "python -c 'from app import create_app, db; from app.utils.seed_db import seed_categories, seed_admin; app = create_app(\"production\"); ctx = app.app_context(); ctx.push(); db.create_all(); seed_categories(); seed_admin()' && gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 2 --timeout 120 'run:app'"]
