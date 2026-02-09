from fastapi import FastAPI
import database_models
from models import Product
from database import SessionLocal, engine
import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello, World!"


products = [
    Product(id=1, name="Laptop", description="A powerful laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A sleek smartphone", price=499.99, quantity=20),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=15),
    Product(id=4, name="Smartwatch", description="A stylish smartwatch", price=299.99, quantity=5),
]

@app.get('/products')
def get_products():
    return products

@app.get('/products/{product_id}')
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}


@app.post('/products')
def create_product(product: Product):
    products.append(product)
    return product

@app.put('/products/{product_id}')
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    return {"error": "Product not found"}


@app.delete('/products/{product_id}')
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            del products[index]
            return {"message": "Product deleted"}
    return {"error": "Product not found"}   

