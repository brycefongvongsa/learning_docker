FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3-venv && \
    python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip3 install pytest

# Make sure the virtual environment is activated when running the container
# adding bin to the PATH ensures the Python interpreter and pip are from the virtual environment
ENV VIRTUAL_ENV=/app/venv
ENV PATH="/app/venv/bin:$PATH"

# Run the application
CMD ["python3", "main.py"]