from datetime import datetime

from pydantic import BaseModel
from pydantic import Field as BaseField
from sqlmodel import Field, SQLModel


class Product(BaseModel):
    name: str = BaseField(min_length=4)
    brand: str
    price: float
    amount: int
    currency: str
    availability: bool
    weight: float
    expiration_date: datetime
    category: str
    image_url: str


class ProductDB(Product, SQLModel, table=True):
    __tablename__ = 'Products'
    id: int = Field(primary_key=True)
    pass
