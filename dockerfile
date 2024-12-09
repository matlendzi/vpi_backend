FROM python:3.10

WORKDIR /app

# Copy the requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app /app/app

# Ensure the certs directory is accessible
# (You will mount the certs directory via Docker Compose)
# Expose the HTTPS port
EXPOSE 443

# Set the command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile", "/app/certs/kartenmitwirkung.de.key", "--ssl-certfile", "/app/certs/fullchain.pem"]
