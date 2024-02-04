from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgres://severin:5eDWCV2Y4tkmiY8iBr76pUSVROyl5dwU@dpg-cmugs8ug1b2c73eibk70-a/user_ebsp"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
