from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import engine, session
from database_models import ProductDB, Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def greeet():
    db = session()
    return 'Anand'

@app.get('/products')
def get_all_products(db: Session = Depends(get_db)):
    return db.query(ProductDB).all()

@app.get('/products/{id}')
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(ProductDB).filter(ProductDB.id == id).first()

    return 'product not found'

@app.post('/products')
def add_product(product: Product, db: Session = Depends(get_db)):
    
    db_product = ProductDB(
        id=product.id,
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )

    db.add(db_product)
    db.commit()

    return {"message": "product added successfully"}

@app.put('/products/{id}')
def update_product(id: int, product: Product, db: Session = Depends(get_db)):

    db_product = db.query(ProductDB).filter(ProductDB.id == id).first()

    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity

        db.commit()

        return {"message": "product updated successfully"}

    return {"error": "product not found"}

@app.delete('/products/{id}')
def delete_product(id: int, db: Session = Depends(get_db)):

    db_product = db.query(ProductDB).filter(ProductDB.id == id).first()

    if db_product:
        db.delete(db_product)
        db.commit()

        return {"message": "product deleted successfully"}

    return {"error": "product not found"}
