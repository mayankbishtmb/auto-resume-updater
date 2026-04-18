# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir requests jinja2

# Make pipeline script executable
RUN chmod +x pipeline.sh

# Default command (runs pipeline)
CMD ["bash", "pipeline.sh"]
