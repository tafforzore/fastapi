from fastapi import APIRouter, Depends, HTTPException, status  # Ajoutez l'importation de status
from sqlalchemy.orm import Session
from models import Post
from crud import create_post, get_post
from database import SessionLocal

router = APIRouter()

@router.post("/posts/", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(post: Post, db: Session = Depends(SessionLocal)):
    return create_post(db, post)

@router.get("/posts/{post_id}", response_model=Post)
async def read_post(post_id: int, db: Session = Depends(SessionLocal)):
    post = get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
