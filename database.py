from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql+psycopg2://neondb_owner:npg_PEm6MUJ0Xdqz@ep-aged-scene-anlvbeiq.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"
engine = create_engine(DATABASE_URL)

session = sessionmaker(autocommit = False, autoflush = False, bind=engine)