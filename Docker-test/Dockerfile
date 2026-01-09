FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
libgl1 \
libmtdev1 \
x11-utils \
libx11-6 \
libxext6 \
libxrender1 \
libxcb1 \
libxkbcommon0 \
&& rm -rf /var/lib/apt/lists/*
COPY . .
CMD ["python", "app.py"]