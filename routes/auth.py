from fastapi import APIRouter
from fastapi.responses import JSONResponse
from icecream import ic
from sqlmodel import Session, select

from config.database import engine
from models.user import User, UserInput
from passwords.password import get_password_hash


def create_access_token():
    return None


auth = APIRouter(prefix='/auth', tags=['Auth'])


@auth.post('/login')
def login_user(user_input: UserInput) -> JSONResponse:
    with Session(engine) as session:
        select_statement = select(User).where(User.email == user_input.email)
        user = session.execute(select_statement).fetchone()
        user = user[0]
        if user is None:
            return JSONResponse({'message': 'User not found'}, 404)
        hashed_pw = get_password_hash(user.password)
        hashed_input = get_password_hash(user_input.password)

        ic(hashed_input)
        ic(hashed_pw)

        if not hashed_pw == hashed_input:
            return JSONResponse({'message': 'Invalid password'}, 400)

    access_token = create_access_token({'email': user.email})

    response = {
        'access_token': access_token,
        'token_type': 'Bearer',
        'message': 'Login successful',
    }

    return JSONResponse(response, 200)
