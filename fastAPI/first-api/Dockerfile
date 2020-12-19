FROM python:alpine3.8

WORKDIR /app
COPY . .

RUN pip install --upgrade -r requirements.txt

EXPOSE 4300
CMD uvicorn main:app --host 0.0.0.0 --port 4303