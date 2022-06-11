FROM python:3.9-slim

RUN apt-get update

WORKDIR /kafka_write_app

COPY ./kafka_write/requirements.txt /kafka_write_app
COPY ./kafka_write/ /kafka_write_app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python3", "main.py"]