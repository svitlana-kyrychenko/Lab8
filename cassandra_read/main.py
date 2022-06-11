from kafka import KafkaConsumer
from json import loads
from cassandra_client import CassandraClient

host = 'cass-node'
port = 9042
keyspace = 'transactions'
client = CassandraClient(host, port, keyspace)
client.connect()

consumer = KafkaConsumer('transactions', bootstrap_servers= 'kafka-server:9092',
                        value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    transaction = message.value
    client.insert_record(['transaction_uid_fraud', 'transaction_uid_date'], transaction)