from typing import Optional

from cryptography.fernet import Fernet
from pydantic import BaseModel, EmailStr
from sqlmodel import Field, SQLModel

SECRET_KEY = 'jSsQVivt5wGaZmQ1rEp1zl15BIYt2waRDZjQHRFLm-4='.encode()
CIPHER = Fernet(SECRET_KEY)


def hash_info(data_to_hash: str) -> str:
    hashed_data = CIPHER.encrypt(data_to_hash.encode())
    return hashed_data.decode()


def decrypt_info(data_to_decrypt: str) -> str:
    data_to_decrypt = data_to_decrypt.encode()
    return CIPHER.decrypt(data_to_decrypt).decode()


def hash_property(property: str) -> str:
    return hash_info(property)


class UserRegister(BaseModel):
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    birth_date: str = Field(alias='birthday')
    email: EmailStr = Field(unique=True)
    password: str

    def encrypt_user(self):
        self.first_name = hash_property(self.first_name)
        self.last_name = hash_property(self.last_name)
        self.birth_date = hash_property(self.birth_date)
        self.email = hash_property(self.email)
        self.password = hash_property(self.password)

    def decrypt_user(self):
        self.first_name = decrypt_info(self.first_name)
        self.last_name = decrypt_info(self.last_name)
        self.birth_date = decrypt_info(self.birth_date)
        self.email = decrypt_info(self.email)
        self.password = decrypt_info(self.password)


class User(UserRegister, SQLModel, table=True):
    __tablename__ = 'Users'
    id: int = Field(default=None, primary_key=True)
    is_admin = Field(default=False)


class UserInput(BaseModel):
    email: EmailStr
    password: str


class UserInputUpdate(UserInput, BaseModel):
    first_name: Optional[str] = Field(alias='firstName')
    last_name: Optional[str] = Field(alias='lastName')
