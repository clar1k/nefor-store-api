from pydantic import BaseModel
from sqlmodel import SQLModel
from datetime import datetime
from sqlmodel import Field

class Product(BaseModel):
  name: str
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
  __tablename__='Products'
  id: int = Field(primary_key=True)
  pass