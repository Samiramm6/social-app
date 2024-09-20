from fastapi import APIRouter
from database.postservice import *
from api import result_message

post_router = APIRouter(prefix="/post", tags=["Post API"])

@post_router.post("/add_post")
async def add_post(user_id: int, main_text: str, hashtag: None):
    result = add_user_post_db(user_id, main_text, hashtag)
    return result_message(result)

@post_router.get("/all_posts")
async def all_posts_api():
    return get_all_posts_db()

@post_router.get("/exact_post")
async def exact_post_api(post_id: int):
    result = get_exact_post_db(post_id)
    return result_message(result)

@post_router.put("/edit_post")
async def edit_post(post_id: int, new_text: str):
    result = change_post_db(post_id, new_text)
    return result_message(result)

@post_router.delete("/delete_post")
async def delete_post_api(post_id: int):
    result = delete_post_db(post_id)
    return result_message(result)