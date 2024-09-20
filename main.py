from fastapi import FastAPI
from api.photo.photo_api import photo_router
from api.users.users_api import user_router
from api.comments.comments_api import comment_router
from api.posts.post_api import post_router
from api.hashtags.hashtags_api import hashtag_router
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(docs_url="/")

app.include_router(photo_router)
app.include_router(user_router)
app.include_router(comment_router)
app.include_router(post_router)
app.include_router(hashtag_router)