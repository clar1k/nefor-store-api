from pydantic import BaseModel


class EmailMessage(BaseModel):
    subject: str
    message: str
