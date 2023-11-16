from typing import Optional

from pydantic import BaseModel, EmailStr
from sqlmodel import Field, SQLModel


class UserRegister(BaseModel):
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    birth_date: str = Field(alias='birthday')
    email: EmailStr = Field(unique=True)
    password: str


class User(UserRegister, SQLModel, table=True):
    __tablename__ = 'Users'
    id: int = Field(default=None, primary_key=True)


class UserInput(BaseModel):
    email: EmailStr
    password: str


class UserInputUpdate(UserInput, BaseModel):
    first_name: Optional[str] = Field(alias='firstName')
    last_name: Optional[str] = Field(alias='lastName')
