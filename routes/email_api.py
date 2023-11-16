from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.email import EmailMessage

email_api = APIRouter(tags=['Email'], prefix='/email')


@email_api.post('/send')
def send_email_to_all_users(message: EmailMessage):
    return JSONResponse({'msg': 'Success'}, 200)
