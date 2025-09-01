from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

PRODUCTS = [
    {
        'id': 1,
        'name': 'IPhone 17',
        'description': 'Last generation',
        'price': 17800.80,
        'available': True
    },
    {
        'id': 2,
        'name': 'Xbox Titan A/W',
        'description': 'Test before the lounch of 2026',
        'price': 6900.90,
        'available': True
    },
    {
        'id': 3,
        'name': 'Notebook',
        'description': 'Special for works 2025',
        'price': 4000.00,
        'available': False
    }
]

class Productt(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    available: Optional[bool] = True


@app.get('/products', tags=['products'])
def list_products() -> list:
    return PRODUCTS


@app.get('/products/available', tags=['products'])
def list_available_products() -> list:
    available_products = []
    for product in PRODUCTS:
        if product['available']:
            available_products.append(product)
    return available_products


@app.get('/products/{product_id}', tags=['products'])
def obtain_products(product_id: int) -> dict:
    for prod in PRODUCTS:
        if prod['id'] == product_id:
            return prod
    return{}


@app.post('/products', tags=['products'])
def create_products(product: Productt) -> dict:
    product = product.dict()
    product['id'] = len(PRODUCTS) + 1
    PRODUCTS.append(product)
    return product


@app.put('/products/{product_id}', tags=['products'])
def upload_products(product_id: int, product: Productt) -> dict:
    for index, prdt in enumerate(PRODUCTS):
        if prdt['id'] == product_id:
            PRODUCTS[index] = product
            return product
    return{}


@app.delete('/products/{product_id}', tags=['products'])
def remove_products(product_id: int) -> dict:
    for index, prdt in enumerate(PRODUCTS):
        if prdt['id'] == product_id:
            PRODUCTS.pop(index)
            return {'message': "This product has been successfully removed."}
    return{}



