FROM python:3.8.3-slim-buster

WORKDIR /usr/src/app
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc cron \
  && apt-get clean

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
