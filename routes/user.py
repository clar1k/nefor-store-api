from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from config.database import engine
from models.user import User, UserRegister
from passwords.password import get_password_hash

user = APIRouter(prefix='/user', tags=['User'])


@user.post('/')
def create_user(new_user: UserRegister) -> JSONResponse:
    new_user.password = get_password_hash(new_user.password)
    db_user = User.parse_obj(new_user.dict())
    db_user.first_name = new_user.first_name
    db_user.last_name = new_user.last_name
    db_user.birth_date = new_user.birth_date
    with Session(engine) as session:
        try:
            session.add(db_user)
            session.commit()
        except IntegrityError as exception:
            print('Exception generated :\n', exception)
            session.rollback()
            return JSONResponse({'msg': 'User is already registered'}, 401)
    return JSONResponse({'msg': 'Success'}, 201)
