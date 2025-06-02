# Use official Python image
FROM python:3.12.0

# Set working directory inside the container
WORKDIR /app

# Copy current folder's contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "main.py"]
