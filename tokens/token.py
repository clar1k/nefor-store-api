from jose import jwt

from config.config import Config


def create_access_token(payload_data: dict) -> str:
    access_token = jwt.encode(
        payload_data.copy(), key=Config.SECRET_KEY, algorithm='HS256'
    )
    return access_token


def decode_access_token(token: str) -> dict:
    payload = jwt.decode(token, key=Config.SECRET_KEY, algorithms=['HS256'])
    return payload
