from fastapi import FastAPI
from DB.database import start_bd
from DB.database import get_db
from routes.routes import blueprint

app = FastAPI()
app.include_router(blueprint)
start_bd(app)

