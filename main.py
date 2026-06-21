from fastapi import FastAPI
from models import Product
from database import session
import database_models

app = FastAPI()

@app.get("/")
def greet():
    return "hey there"

products = [
    Product(id=1, name="iPhone", description="Version 17", price=1000, quantity=50),
    Product(id=2, name="Pixel", description="Version 10", price=100, quantity=50),
    Product(id=3, name="Samsung", description="Version 25", price=400, quantity=40),
    Product(id=7, name="RedMi", description="Version 6", price=10, quantity=5)
]


@app.get("/products")
def get_all_products():
    # db connection
    db = session()
    # query
    db.query()
    return products

@app.get("/product/{id}")
def get_product(id: int):
    # if (id > products.length), throw an error
    for product in products:
        if product.id == id:
            return product
    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product added successfully"

    return "product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted successfully"

    return "product not found"
