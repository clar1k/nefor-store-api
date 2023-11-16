from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

from config.database import engine
from models.user import User, UserInput
from passwords.password import get_password_hash
from tokens.token import create_access_token

auth = APIRouter(prefix='/auth', tags=['Auth'])


@auth.post('/login')
def login(user_input: UserInput) -> JSONResponse:
    with Session(engine) as session:
        select_statement = select(User).where(User.email == user_input.email)
        user = session.execute(select_statement).first()
        user = user[0]
        if user is None:
            return JSONResponse({'message': 'User not found'}, 404)
        hashed_pw = get_password_hash(user.password)
        if not hashed_pw == user_input.password:
            return JSONResponse({'message': 'Invalid password'}, 400)

    access_token = create_access_token({'email': user.email})

    response = {
        'access_token': access_token,
        'token_type': 'Bearer',
        'message': 'Login successful',
    }

    return JSONResponse(response, 200)
