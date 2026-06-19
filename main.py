from fastapi import FastAPI
from models import Product

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
    return products

@app.get("/product/{id}")
def get_product(id: int):
    # if (id > products.length), throw an error
    for product in products:
        if product.id == id:
            return product
    return products[id-1]

@app.post("/product")
def add_product(product: Product):
    products.append(product)
