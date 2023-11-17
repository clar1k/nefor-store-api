import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse

product = APIRouter(prefix='/items', tags=['Product'])

with open('dummy-data.json') as file:
    content = file.read()
    content = json.loads(content)


@product.get('')
def get_items(page: int = 0):
    return JSONResponse(content, 200)


@product.get('/{item_id}')
def get_item_by_id(item_id: int):
    return JSONResponse(content[item_id], 200)
