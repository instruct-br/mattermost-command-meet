FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && \
  apk add --no-cache --virtual .build-deps gcc musl-dev bash

RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /code

ADD Pipfile Pipfile.lock /code/
RUN pipenv install --system

ADD src/ /code/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
