import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlmodel import Session, delete, update

from config.database import engine
from models.product import Product, ProductDB

product = APIRouter(prefix='/items', tags=['Product'])

with open('dummy-data.json') as file:
    content = file.read()
    content = json.loads(content)


@product.get('')
def get_product(page: int = 0) -> JSONResponse:
    return JSONResponse(content, 200)


@product.get('/{product_id}')
def get_product_by_id(product_id: int) -> JSONResponse:
    return JSONResponse(content[product_id], 200)


@product.post('')
def create_product(product: Product) -> JSONResponse:
    with Session(engine) as session:
        prod = ProductDB().parse_obj(product)
        session.add(prod)
        session.commit()
    return JSONResponse({'msg': 'Created product'}, 201)


@product.delete('/{product_id}')
def delete_product_by_id(product_id: int) -> JSONResponse:
    with Session(engine) as session:
        delete_statement = delete(ProductDB).where(ProductDB.id == product_id)
        session.execute(delete_statement)
        session.commit()
    return JSONResponse({'msg': 'Deleted product'}, 200)


@product.put('/{product_id}')
def update_product_by_id(product_id: int, product: Product) -> JSONResponse:
    with Session(engine) as session:
        update_statement = (
            update(ProductDB).where(ProductDB.id == product_id).values(product.json())
        )
        session.execute(update_statement)
        session.commit()
    return JSONResponse({'msg': 'Updated product'}, 200)
