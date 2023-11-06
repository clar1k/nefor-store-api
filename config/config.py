from os import environ as env
from dotenv import load_dotenv

load_dotenv('.env.prod')

class Config:
    DATABASE_URL=env.get('DATABASE_URL')
    SECRET_KEY=env.get('SECRET_KEY')