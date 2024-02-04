from fastapi import FastAPI, HTTPException, Depends
from databases import Database
from sqlalchemy.orm import sessionmaker

from database import database
from models import users

app = FastAPI()

# Fonction de dépendance pour obtenir la session de la base de données
def get_db():
    db = None
    try:
        db = database
        yield db
    finally:
        db.close()

# Point de terminaison FastAPI utilisant la base de données
@app.get("/users/{user_id}")
async def read_user(user_id: int, db: Database = Depends(get_db)):
    query = users.select().where(users.c.id == user_id)
    user = await db.fetch_one(query)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
