from typing import Optional
from pydantic import EmailStr
from sqlmodel import Field, SQLModel, create_engine
from config.config import Config


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    birth_date: str = Field(alias='birthday')
    # adress: str
    # role: str
    # phone_number: str
    email: EmailStr
    password: str
    # password_salt: str


engine = create_engine('sqlite:///nefor.db')
def create_db() -> None:
    SQLModel.metadata.create_all(engine)
    