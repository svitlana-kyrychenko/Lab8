FROM python:3.9-slim

RUN apt-get update

WORKDIR /cassandra_read_app

COPY ./cassandra_read/requirements.txt /cassandra_read_app
COPY ./cassandra_read/ /cassandra_read_app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python3", "main.py"]