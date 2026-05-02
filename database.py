from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Anand%40358@localhost:5432/product_db"
engine = create_engine(DATABASE_URL)

session = sessionmaker(autocommit = False, autoflush = False, bind=engine)

