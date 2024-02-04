from sqlalchemy import select, insert, update, delete
from database import database
from models import users

async def create_user(name: str):
    query = users.insert().values(name=name)
    return await database.execute(query)

async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

async def update_user(user_id: int, new_name: str):
    query = users.update().where(users.c.id == user_id).values(name=new_name)
    return await database.execute(query)

async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    return await database.execute(query)
