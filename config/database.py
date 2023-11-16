import logging

from sqlmodel import SQLModel, create_engine

logging.basicConfig(filename='sql.log')
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = create_engine('sqlite:///nefor.db', echo=False)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
