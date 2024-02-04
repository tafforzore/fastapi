from fastapi import APIRouter, HTTPException, Depends
from ..DB.database import users,get_db
from sqlalchemy.orm import sessionmaker
from databases import Database

blueprint = APIRouter()
@blueprint.get("/users/{user_id}")
async def read_user(user_id: int, db: Database = Depends(get_db)):
    query = users.select().where(users.c.id == user_id)
    user = await db.fetch_one(query)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user