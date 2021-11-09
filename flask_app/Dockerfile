FROM python:3.8.10-slim-buster

WORKDIR /app

COPY . /app

RUN  apt-get -y update
RUN  apt-get -y install gcc
RUN  apt-get -y install python3-dev build-essential

RUN pip install -r requirements.txt
RUN mkdir /tmp/final-metodos
CMD ["uwsgi", "app.ini"]