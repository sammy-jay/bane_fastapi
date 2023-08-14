from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db, engine
from app.schemas import users
from app.lib import users as usersLib
from app.models.user import User
from app.models.address import Address

User.metadata.create_all(bind=engine)
Address.metadata.create_all(bind=engine)

router = APIRouter(prefix="/users", tags=["Users"])



# @router.get("/{post_id}")
# def getPostById(post_id: int, db: Session = Depends(get_db)):
#     db_post = postsLib.getPostById(db, post_id)
#     if db_post is None:
#         return HTTPException(status_code=404, detail=f"Post with id {post_id} no found")
#     return {"data": db_post}

# @router.post("/", status_code=status.HTTP_201_CREATED)
# def createPost(post: posts.PostCreate, db: Session = Depends(get_db)):
#     db_post = postsLib.createPost(db, post)
#     return {"data": db_post} 
