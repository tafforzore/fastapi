from sqlalchemy.orm import Session
from models import Post

def create_post(db: Session, post: Post):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()
