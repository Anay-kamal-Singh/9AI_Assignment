from fastapi import FastAPI
from . import models, crud, db

app = FastAPI()

db.connect_to_mongo()

# CRUD operations for blog posts
@app.post("/posts/", response_model=models.Post)
async def create_post(post: models.PostCreate):
    return crud.create_post(post)

@app.get("/posts/{post_id}", response_model=models.Post)
async def read_post(post_id: str):
    return crud.get_post(post_id)

# CRUD operations for comments
@app.post("/posts/{post_id}/comments/", response_model=models.Comment)
async def create_comment(post_id: str, comment: models.CommentCreate):
    return crud.create_comment(post_id, comment)

# CRUD operations for likes
@app.post("/posts/{post_id}/like/")
async def like_post(post_id: str):
    return crud.like_post(post_id)
