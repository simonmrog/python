FROM python:3.6.6-slim-stretch

# Set working directory and install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt

# Copy app
COPY api api
EXPOSE 3001
CMD python ./api/app.py