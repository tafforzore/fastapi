from fastapi import FastAPI
from DB import models
from DB.database import SessionLocal, engine
from routes.routes import blueprint

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(blueprint)
# Dependency

