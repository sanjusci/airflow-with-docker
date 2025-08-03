# Use the official Apache Airflow image as the base image
FROM apache/airflow:2.9.1

# Copy the requirements file into the image
COPY requirements.txt /requirements.txt

# Upgrade pip to the latest version for the user
RUN pip install --upgrade pip

# Install Python dependencies from requirements.txt for the user
RUN pip install --no-cache-dir -r /requirements.txt