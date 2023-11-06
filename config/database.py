from sqlmodel import SQLModel, create_engine


engine = create_engine('sqlite:///nefor.db')

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)