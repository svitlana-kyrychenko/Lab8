def get_fraud_transactions(self, uid):
    query = f"SELECT * FROM transaction_fraud_uid WHERE nameOrig='{uid}' AND isFraud=1"
    rows = self.session.execute(query)
    return list(rows)


def get_largest_transactions(self, uid):
    query = f"SELECT * FROM transaction_fraud_uid WHERE nameOrig='{uid}'"
    rows = list(self.session.execute(query))
    sortedList = sorted(rows, reverse=True, key=lambda d: d['amount'])
    return sortedList[:3]


def get_transactions_by_date(self, uid, start_date, end_date):
    query = f"SELECT * FROM transaction_date_uid WHERE nameDest='{uid}' AND transactionDate > '{start_date}' AND transactionDate < '{end_date}'"
    rows = list(self.session.execute(query))
    sum_transactions = sum([t['amount'] for t in rows])
    return sum_transactions

def insert_record(self, tables, dct):
    for table in tables:
        query = f"INSERT INTO {table} (step ,  type_transaction ,  amount , \
                                nameOrig ,  oldbalanceOrg ,  newbalanceOrig , \
                                nameDest ,  oldbalanceDest ,  newbalanceDest , \
                                isFraud ,  isFlaggedFraud ,  transactionDate ) \
                                VALUES ({dct['step']}, '{dct['type_transaction']}', {dct['amount']}, \
                                '{dct['nameOrig']}', {dct['oldbalanceOrg']},  {dct['newbalanceOrig']}, \
                                '{dct['nameDest']}', {dct['oldbalanceDest']}, {dct['newbalanceDest']}, \
                                {dct['isFraud']}, {dct['isFlaggedFraud']}, '{dct['transactionDate']}')"
        self.execute(query)