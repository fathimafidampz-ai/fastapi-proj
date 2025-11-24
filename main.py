from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products = [
    Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop", quantity=10),
    Product(id=2, name="Smartphone", price=499.99, description="A latest model smartphone", quantity=25),
    Product(id=3, name="Headphones", price=199.99, description="Noise-cancelling headphones", quantity=15),
    Product(id=4, name="Monitor", price=299.99, description="4K UHD Monitor", quantity=8),
    Product(id=5, name="Keyboard", price=49.99, description="Mechanical keyboard", quantity=30),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_products_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"message": "Product not found"}

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i] = product
            return "product added successfully"
    return {"message": "Product not found"}



@app.delete("/product/{id}")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            del products[index]
            return {"message": "Product deleted successfully"}
    return {"message": "Product not found"}
