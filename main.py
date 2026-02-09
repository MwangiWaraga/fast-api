from fastapi import FastAPI, HTTPException, status
from typing import List

import database_models
from database import engine
from models import Product

app = FastAPI(title="FastAPI Products")

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message": "Hello, World!"}


products: List[Product] = [
    Product(id=1, name="Laptop", description="A powerful laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A sleek smartphone", price=499.99, quantity=20),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=15),
    Product(id=4, name="Smartwatch", description="A stylish smartwatch", price=299.99, quantity=5),
]


@app.get("/products", response_model=List[Product])
def get_products():
    return products


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    if any(p.id == product.id for p in products):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product ID already exists")
    products.append(product)
    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            del products[index]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

