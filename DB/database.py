from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
metadata = MetaData()
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def start_bd(app):
    @app.on_event("startup")
    def startup_db():
        engine.connect()

    @app.on_event("shutdown")
    def shutdown_db():
        engine.close()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()