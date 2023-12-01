import logging
from config.config import Config
from sqlmodel import SQLModel, create_engine

logging.basicConfig(filename='sql.log', level=logging.INFO)
engine = create_engine(Config.DATABASE_URL)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
