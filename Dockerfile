# Base Image
FROM python:3.9-slim

# Set environment variables to reduce image size and python cache
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System Dependencies (Merged RUN commands)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy Requirements
COPY requirements.txt .

# Install Dependencies (No cache & remove wheel cache)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy Application Files
COPY . .

# Streamlit Port
EXPOSE 8501

# Run Streamlit App
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.fileWatcherType=none"]
