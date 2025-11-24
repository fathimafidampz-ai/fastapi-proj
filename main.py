from fastapi import FastAPI
from models import Product

app =FastAPI()
@app.get("/")
def greet():
    return "Hello, World!"


products = [
    Product(1, "Laptop", 999.99, "A high-performance laptop", 10),
    Product(2, "Smartphone", 499.99, "A latest model smartphone", 25),
    Product(3, "Headphones", 199.99, "Noise-cancelling headphones", 15),    
    Product(4, "Monitor", 299.99, "4K UHD Monitor", 8),
    Product(5, "Keyboard", 49.99, "Mechanical keyboard", 30 )
    
]


@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_products_by_id(id: int):
    for product in products:
        if product.id == id:    
            return product
            
    return "Product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.delete("/product/{id}")
def delete_product(id: int):