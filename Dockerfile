FROM python:3.11.5-slim
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY requirements.txt /tmp
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt

WORKDIR /code
COPY . /code
