# pull official base image
FROM python:3.8.3-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]

# add app
COPY . .

# run entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
