FROM python:3.6.6-slim-stretch

COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt

COPY api api

ENTRYPOINT [ "python3.6", "/api/app.py" ]
