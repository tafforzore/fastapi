from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

DATABASE_URL = "postgres://severin:5eDWCV2Y4tkmiY8iBr76pUSVROyl5dwU@dpg-cmugs8ug1b2c73eibk70-a/user_ebsp"
conn = psycopg2.connect(DATABASE_URL)
try:
    print("Connected to the database")
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()
