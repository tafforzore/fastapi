from fastapi import FastAPI
from DB.database import start_bd

from DB.database import get_db

app = FastAPI()
start_bd(app)

