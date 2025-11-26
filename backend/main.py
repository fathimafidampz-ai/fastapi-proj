from fastapi import FastAPI, HTTPException
from models import Product
from database import products_collection
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def serialize_product(product):
    product["_id"] = str(product["_id"])
    return product


@app.get("/")
def greet():
    return "Hello, World!"

@app.get("/products")
def get_all_products():
    products = list(products_collection.find())
    return [serialize_product(p) for p in products]
  
  
@app.get("/products/{id}")
def get_product_by_id(id: str):
    product = products_collection.find_one({"_id": ObjectId(id)})
    if product:
        return serialize_product(product)
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products")
def add_product(product: Product):
    result = products_collection.insert_one(product.dict())
    return {"message": "Product added successfully", "id": str(result.inserted_id)}

@app.put("/products/{id}")
def update_product(id: str, product: Product):
    result = products_collection.update_one({"_id": ObjectId(id)}, {"$set": product.dict()})
    if result.modified_count:
        return {"message": "Product updated successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{id}")
def delete_product(id: str):
    result = products_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")
