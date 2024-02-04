from fastapi import APIRouter, HTTPException, Depends
from crud import create_user, read_user, update_user, delete_user

user_router = APIRouter()

@user_router.post("/", response_model=dict)
async def create_user_api(name: str):
    user_id = await create_user(name)
    return {"user_id": user_id}

@user_router.get("/{user_id}", response_model=dict)
async def read_user_api(user_id: int):
    user = await read_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/{user_id}", response_model=dict)
async def update_user_api(user_id: int, new_name: str):
    updated_user = await update_user(user_id, new_name)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@user_router.delete("/{user_id}", response_model=dict)
async def delete_user_api(user_id: int):
    deleted_user = await delete_user(user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
