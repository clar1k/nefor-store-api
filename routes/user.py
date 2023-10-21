from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import engine, User
from sqlmodel import Session
from passwords.password import get_password_hash
from sqlalchemy.exc import IntegrityError

user = APIRouter(prefix='/user', tags=['User'])


@user.post('/')
def create_user(new_user: User) -> JSONResponse:
    new_user.password = get_password_hash(new_user.password)
    
    with Session(engine) as session:
        try:
            session.add(new_user)
            session.commit()
        except IntegrityError as exception:
            print('Exception generated :\n', exception)
            session.rollback()
            return JSONResponse({'msg': 'User is already registered'}, 401)
    
    return JSONResponse({'msg': 'Success'}, 201)


@user.put('/')
def update_user_info() -> JSONResponse:
    return