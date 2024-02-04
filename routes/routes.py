from fastapi import APIRouter, HTTPException, Depends
from databases import Database
from DB.models import Users
from DB.database import get_db
from sqlalchemy.orm import Session

blueprint = APIRouter()
# @blueprint.get("/users/{user_id}")
# async def read_user(user_id: int, db: Database = Depends(get_db)):
#     query = users.select().where(users.c.id == user_id)
#     user = await db.fetch_one(query)
    
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

@blueprint.post("/create_user/")
def create_user(item: Users, db: Session = Depends(get_db)):
    print('ok')
    db_item = Users(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item