FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
