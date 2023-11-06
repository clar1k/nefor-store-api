from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.product import Product, ProductDB
import json
product = APIRouter(prefix='/items', tags=['Product'])


@product.get('')
def get_items(page: int = 0):
  with open('dummy-data.json') as file:
    content = file.read()
    
  content = json.loads(content)
  return JSONResponse(content, 200)


@product.post('/add')
def add_product():
  return JSONResponse()