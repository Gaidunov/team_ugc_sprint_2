FROM python:3.10-slim

WORKDIR /app

RUN apt update
RUN apt --assume-yes install libpq-dev

COPY ./docker/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./app/api /app/api

