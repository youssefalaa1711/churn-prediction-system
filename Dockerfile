FROM python:3.11-slim

# 1. Set working directory
WORKDIR /app

# 2. Copy requirements first (layer caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy project code
COPY artifacts ./artifacts
COPY backend ./backend

# 4. Expose FastAPI port
EXPOSE 8000

# 5. Run FastAPI
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
