ROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/Pipfile
RUN pipenv sync
RUN pipenv shell

COPY ./recipebook /usr/src/app
