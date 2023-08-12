from fastapi import APIRouter, Depends, status, HTTPException

from app.schemas import posts
from app.lib import posts as postsLib

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/")
def getAllPosts():
    all_posts = postsLib.getAllPosts()
    return {"data": all_posts}

@router.get("/{post_id}")
def getPostById(post_id: int):
    post = postsLib.getPostById(post_id)

    if post:
        return {"data": post}
    return HTTPException(status_code=404, detail=f"Post with id {post_id} no found")

@router.post("/", status_code=status.HTTP_201_CREATED)
def createPost(post: posts.PostCreate):
    return postsLib.createPost(post)

@router.patch("/{post_id}")
def updatePost(post_id: int, post: posts.PostUpdate):
    updated_post = postsLib.updatePost(post_id, post)

    if updated_post:
        return {"data": updated_post}
    return HTTPException(status_code=404, detail=f"Post with id {post_id} no found")

@router.delete("/{post_id}", status_code=204)
def deletePost(post_id: int):
    post = postsLib.deletePost(post_id)

    if post:
        return {"data": {}}
    return HTTPException(status_code=404, detail=f"Post with id {post_id} no found")