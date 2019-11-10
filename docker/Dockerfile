FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /work
WORKDIR /work

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /work
