from cassandra.query import dict_factory
from cassandra.cluster import Cluster
import query

class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)
        self.session.row_factory = dict_factory

    def execute(self, query):
        self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def insert_record(self, tables, dct):
        query.insert_record(self, tables, dct)

    def get_fraud_transactions(self, uid):
        query.get_fraud_transactions(self, uid)

    def get_largest_transactions(self, uid):
        query.get_largest_transactions(self, uid)

    def get_transactions_by_date(self, uid, start_date, end_date):
        query.get_transactions_by_date(self, uid, start_date, end_date)