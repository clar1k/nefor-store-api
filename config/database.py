from typing import Optional
from pydantic import EmailStr, BaseModel
from sqlmodel import Field, SQLModel, Session, create_engine


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    birth_date: str = Field(alias='birthday')
    email: EmailStr = Field(unique=True)
    # adress: str
    # role: str
    # phone_number: str
    password: str
    # password_salt: str


class UserInput(BaseModel):
    email: EmailStr
    password: str


engine = create_engine('sqlite:///nefor.db')
session = Session(bind=engine)

def create_db() -> None:
    SQLModel.metadata.create_all(engine)