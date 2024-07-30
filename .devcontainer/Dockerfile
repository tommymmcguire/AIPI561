# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /workspace

# Copy the current directory contents into the container at /workspace
COPY . /workspace

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install additional development tools
RUN pip install flake8 pytest

# Expose port 5001 for the Flask app
EXPOSE 5001

# Set up the environment
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

# Run the Flask app by default
CMD ["python", "src/app.py"]
