FROM python:3.10-alpine

WORKDIR /app

# Install required system dependencies
RUN apk add --no-cache libstdc++

# Only required runtime dependencies
RUN apk add --no-cache libffi libjpeg-turbo zlib

# Install latest stable PyMuPDF that provides a wheel
RUN pip install --no-cache-dir "PyMuPDF>=1.21.1"

COPY . .

CMD ["python", "main.py"]
