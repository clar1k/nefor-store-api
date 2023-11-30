from os import environ as env

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv('.env.dev')


class Config:
    DATABASE_URL = env.get('DATABASE_URL')
    SECRET_KEY = env.get('SECRET_KEY')
    SMTP_HOST = env.get('SMTP_HOST')
    SMTP_PORT = env.get('SMTP_PORT')
    SMTP_USERNAME = env.get('SMTP_USERNAME')
    SMTP_PASSWORD = env.get('SMTP_PASSWORD')


class JWTSettings(BaseModel):
    authjwt_secret_key: str = env.get('SECRET_KEY')
