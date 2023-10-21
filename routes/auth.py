from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlmodel import select
from passwords.password import verify_password

from config.database import UserInput, User, session
from tokens.token import create_access_token

auth = APIRouter(prefix='/auth', tags=['Auth'])


@auth.post('/register')
async def register() -> JSONResponse:
    return


@auth.post('/login')
def login(user_input: UserInput) -> JSONResponse:
    select_user_statement = select(User).where(User.email == user_input.email)
    user: User = session.exec(select_user_statement).first()
    
    if not user:
        return JSONResponse({'msg':'User not found'}, 400)
    
    password_is_incorrect = not verify_password(user_input.password, user.password)
    
    if password_is_incorrect:
        return JSONResponse({'msg': 'Wrong password'}, 400)
    
    access_token = create_access_token({'sub': user.id})
    
    return JSONResponse({'access_token': access_token}, 200)


@auth.get('/refresh')
def refresh_token() -> JSONResponse:
    return