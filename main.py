from fastapi import FastAPI, HTTPException, Depends
from databases import Database
from sqlalchemy.orm import sessionmaker

from DB.database import database
from DB.models import users

from DB.database import get_db

app = FastAPI()

