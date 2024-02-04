from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
)

metadata.create_all(bind=engine)
database = Database(DATABASE_URL)

def get_db():
    db = None
    try:
        db = database
        yield db
    finally:
        db.close()