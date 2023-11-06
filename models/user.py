from typing import Optional
from pydantic import EmailStr, BaseModel
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    __tablename__='Users'
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    birth_date: str = Field(alias='birthday')
    email: EmailStr = Field(unique=True)
    password: str
    # password_salt: str
    # adress: str
    # role: str
    # phone_number: str


class UserInput(BaseModel):
    email: EmailStr
    password: str