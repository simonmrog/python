# Docker base image
FROM python:alpine3.8

# Set working directory
WORKDIR /app
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Copy and run app
EXPOSE 4200
CMD python ./main.py
