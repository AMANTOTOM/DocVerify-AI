# Start from a small Python image
FROM python:3.12-slim

# Work inside the /app folder in the container
WORKDIR /app

# Install the packages first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY . .

# The app listens on port 8000
EXPOSE 8000

# Start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]