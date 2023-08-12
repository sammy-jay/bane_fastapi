from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.schemas import posts
from app.lib import posts as postsLib
from app.models.post import Post

Post.metadata.create_all(bind=engine)

router = APIRouter(prefix="/posts", tags=["Posts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def getAllPosts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    all_posts = postsLib.getAllPosts(db, skip=skip, limit=limit)
    return {"data": all_posts}

@router.get("/{post_id}")
def getPostById(post_id: int, db: Session = Depends(get_db)):
    db_post = postsLib.getPostById(db, post_id)
    if db_post is None:
        return HTTPException(status_code=404, detail=f"Post with id {post_id} no found")
    return {"data": db_post}

@router.post("/", status_code=status.HTTP_201_CREATED)
def createPost(post: posts.PostCreate, db: Session = Depends(get_db)):
    db_post = postsLib.createPost(db, post)
    return {"data": db_post} 

@router.patch("/{post_id}")
def updatePost(post_id: int, post: posts.PostUpdate, db: Session = Depends(get_db)):
    db_post = postsLib.updatePost(db, post_id, post)
    if db_post is None:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} no found")
    return {"data": db_post}

@router.delete("/{post_id}", status_code=204)
def deletePost(post_id: int, db: Session = Depends(get_db)):
    db_post = postsLib.deletePost(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} no found")
    return {"data": {}}