from jose import jwt
from config.config import Config


def create_access_token(data: dict):
    access_token = jwt.encode(data.copy(), key=Config.SECRET_KEY, algorithm='HS256')
    return access_token