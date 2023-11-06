from fastapi import APIRouter
from fastapi.responses import JSONResponse


from models.user import UserInput

auth = APIRouter(prefix='/auth', tags=['Auth'])


@auth.post('/register')
async def register() -> JSONResponse:
    return


@auth.post('/login')
def login(user_input: UserInput) -> JSONResponse:
    raise NotImplementedError


@auth.get('/refresh')
def refresh_token() -> JSONResponse:
    return