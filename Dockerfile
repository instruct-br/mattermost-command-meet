FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && \
  apk add --virtual .build-deps gcc musl-dev bash

RUN pip install --upgrade pip
RUN pip install pipenv

RUN mkdir /code
WORKDIR /code

ADD Pipfile Pipfile.lock /code/
RUN pipenv install --system

ADD src/ /code/
