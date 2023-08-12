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

def getAllPosts():
    return all_posts

def getPostById(post_id: int):
    post = findPost(post_id)
    if post:
        return post
   
    return False

def createPost(post: posts.PostCreate):
    new_post = {
        "id": len(all_posts) + 1,
        **post.model_dump()
    }
    all_posts.append(new_post)
    return new_post

def updatePost(post_id: int, post: posts.PostUpdate):
    found_post = findPost(post_id)
    if found_post:
        return found_post
   
    return False

def deletePost(post_id: int):
    found_post = findPost(post_id)
    if found_post:
        return found_post
   
    return False