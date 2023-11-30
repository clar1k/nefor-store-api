from fastapi import APIRouter
from fastapi.responses import JSONResponse
from icecream import ic
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, delete, update


from config.database import engine
from models.user import User, UserRegister
from passwords.password import hash_info

user = APIRouter(prefix='/user', tags=['User'])


@user.post('/')
def create_user(new_user: UserRegister) -> JSONResponse:
    new_user.password = hash_info(new_user.password)
    db_user = User.parse_obj(new_user.dict())
    db_user.first_name = new_user.first_name
    db_user.last_name = new_user.last_name
    db_user.birth_date = new_user.birth_date
    ic(db_user)
    with Session(engine) as session:
        try:
            session.add(db_user)
            session.commit()
        except IntegrityError as exception:
            print('Exception generated :\n', exception)
            session.rollback()
            return JSONResponse({'msg': 'User is already registered'}, 401)
    return JSONResponse({'msg': 'Created user'}, 201)


@user.put('/{user_id}')
async def update_user_by_id(user: UserRegister, user_id: int) -> JSONResponse:
    with Session(engine) as session:
        update_stmnt = (
            update(User)
            .where(User.id == user_id)
            .values(
                first_name=user.first_name,
                email=user.email,
                last_name=user.last_name,
                birth_date=user.birth_date,
                password=hash_info(user.password),
            )
        )
        session.execute(update_stmnt)
        session.commit()
    return JSONResponse({'msg': 'Update success'}, 200)


@user.delete('/{user_id}')
def delete_user_by_id(user_id: int) -> JSONResponse:
    with Session(engine) as session:
        delete_stmnt = delete(User).where(User.id == user_id)
        session.execute(delete_stmnt)
        session.commit()
    return JSONResponse({'msg': 'Delete success'}, 200)
