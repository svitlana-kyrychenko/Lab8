from kafka import KafkaProducer
from json import dumps
import csv
import datetime
import random

producer = KafkaProducer(bootstrap_servers='kafka-server:9092',
                         value_serializer=lambda x:
                         dumps(x).encode('ascii'))

with open('PS_20174392719_1491204439457_log.csv', 'r') as f:
    file = csv.reader(f)
    header = next(file)
    for row in file:
        row_dict = dict(zip(header, row))

        random_num_days = random.randrange(30)
        random_date = datetime.datetime.now() - datetime.timedelta(days=random_num_days)

        row_dict['transactionDate'] = random_date.strftime("%Y-%m-%d")
        producer.send('transactions', row_dict)
        producer.flush()