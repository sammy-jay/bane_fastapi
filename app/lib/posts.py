from sqlalchemy.orm import Session
from app.schemas import posts
from app.models.post import Post


all_posts: list[posts.Post] = []
last_id = 1

def findPost(post_id: int):
    for post in all_posts:
        if post['id'] == post_id:
            return post
    return None

def getAllPosts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()

def getPostById(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        return db_post

    return None

def createPost(db: Session, post: posts.PostCreate):
    db_post = Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def updatePost(db: Session, post_id: int, post: posts.PostUpdate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        for key, value in post.model_dump().items():
            setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
        return db_post
    return None

def deletePost(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return db_post
    return None