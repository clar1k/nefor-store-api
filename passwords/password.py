from cryptography.fernet import Fernet
from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


SECRET_KEY = 'jSsQVivt5wGaZmQ1rEp1zl15BIYt2waRDZjQHRFLm-4='.encode()
CIPHER = Fernet(SECRET_KEY)


def get_password_hash(plain_password: str):
    return hash_info(plain_password)


def hash_info(data_to_hash: str) -> str:
    print(data_to_hash)
    hashed_data = CIPHER.encrypt(data_to_hash.encode())
    return hashed_data.decode()


def decrypt_info(data_to_decrypt: str) -> str:
    data_to_decrypt = data_to_decrypt.encode()
    decrypted_data = CIPHER.decrypt(data_to_decrypt).decode()
    return decrypted_data
