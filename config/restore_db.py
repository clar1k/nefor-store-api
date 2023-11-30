import re
from typing import List

from sqlalchemy import create_engine, text

db_uri = 'sqlite:///logs-test.db'
engine = create_engine(db_uri, echo=False)

sql_query = """
    CREATE TABLE "Users" (
	first_name VARCHAR NOT NULL, 
	last_name VARCHAR NOT NULL, 
	birth_date VARCHAR NOT NULL, 
	email VARCHAR NOT NULL, 
	password VARCHAR NOT NULL, 
	id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
)"""


def create_tables() -> None:
    engine.execute(text(sql_query))


def filter_query(transaction: str) -> str:
    transaction = re.sub(r'\n', '', transaction)
    transaction = re.sub('VALUES \([^)]+\)', 'VALUES', transaction)
    transaction = re.sub('COMMIT', '', transaction)
    return transaction


def get_logs(logs_filename: str) -> str:
    with open('sql.log', 'r', encoding='utf-8') as file:
        logs = file.read()
    return logs


def filter_logs(logs: str) -> List[str]:
    logs = re.sub('INFO:sqlalchemy.engine.Engine:', '', logs)
    logs = re.sub(r'\[.*?\]', '', logs)
    logs = logs.split('BEGIN (implicit)')
    return logs


def execute_statements(transactions: List[str], engine):
    for transaction in transactions:
        if 'PRAGMA' in transaction:
            continue
        transaction = filter_query(transaction)
        sql_query = text(transaction)
        try:
            engine.execute(sql_query)
        except Exception as e:
            print(e)


def restore_database_from_logs(db_uri: str, logs_filename: str) -> None:
    logs = get_logs(logs_filename)
    transactions: List[str] = filter_logs(logs)
    execute_statements(transactions, engine)


def main() -> None:
    create_tables()
    restore_database_from_logs('sqlite:///logs-test.db', 'sql.log')


if __name__ == '__main__':
    main()
