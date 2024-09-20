from database.models import UserPost, Comment, Hashtags
from database import get_db



# ф-ия для создания поста
def add_user_post_db(user_id, main_text, hashtag=None):
    with next(get_db()) as db:
        new_post = UserPost(user_id=user_id, main_text=main_text,
                            hashtag=hashtag)
        db.add(new_post)
        db.commit()
        return new_post.id

# ф-ия для получения всех постов
def get_all_posts_db():
    with next(get_db()) as db:
        get_all_posts = db.query(UserPost).all()
        return get_all_posts

# ф-мя для получения опр постапо айди
def get_exact_post_db(post_id):
    with next(get_db()) as db:
        exact_post = db.query(UserPost).filter_by(id=post_id).first()
        if exact_post:
            return exact_post
        return False

# ф-ия для изм текста поста
def change_post_db(post_id, new_text):
    with next(get_db()) as db:
        post_to_edit = db.query(UserPost).filter_by(id=post_id).first()
        if post_to_edit:
            post_to_edit.main_text = new_text
            db.commit()
            return True
        return False

# ф-ия для удаления поста
def delete_post_db(post_id):
    with next(get_db()) as db:
        delete_post = db.query(UserPost).filter_by(id=post_id).first()
        if delete_post:
            db.delete(delete_post)
            db.commit()
            return delete_post
        return False

# ф-ия для добавления ком
def add_comment_to_post_db(user_id, post_id, text):
    with next(get_db()) as db:
        new_comment = Comment(comment=text, user_id=user_id, post_id=post_id)
        db.add(new_comment)
        db.commit()
        return new_comment.id

# ф-ия для получения ком опр поста
def get_comment_by_post_id_db(post_id):
    with next(get_db()) as db:
        exact_post = db.query(UserPost).filter_by(id=post_id).first()
        if exact_post:
            get_comment = db.query(Comment).filter_by(post_id=post_id).all()
            return get_comment
        return False

# ф-ия для добавления хештега
def add_hashtag_db(hashtag_name):
    with next(get_db()) as db:
        add_hashtag = Hashtags(hashtag_name=hashtag_name)
        db.add(add_hashtag)
        db.commit()
        return add_hashtag.id

# ф-ия для получения топ постов по хеш
def get_post_by_hashtag_db(size, hashtag_name):
    with next(get_db()) as db:
        exact_hashtag = db.query(Hashtags).filter_by(hashtag_name=hashtag_name).first()
        if exact_hashtag:
            exact_posts = db.query(UserPost).filter_by(hashtag=hashtag_name).limit(size).all()
            return exact_posts

# ф-ия для получения хеш по назв
def get_hashtag_db(hashtag_name):
    with next(get_db()) as db:
        exact_hashtag = db.query(Hashtags).filter_by(hashtag_name=hashtag_name).first()
        if exact_hashtag:
            return exact_hashtag
        return False

# ф-ия для изм текста ком
def change_comment_text_db(comment_id, new_text):
    with next(get_db()) as db:
        comment = db.query(Comment).filter_by(id=comment_id).first()
        if comment:
            comment.comment = new_text
            db.commit()
            return True
        return False

# ф-ия для удаления ком по id
def delete_comment_db(comment_id):
    with next(get_db()) as db:
        delete_comment = db.query(Comment).filter_by(id=comment_id).first()
        if delete_comment:
            db.delete(delete_comment)
            db.commit()
            return True
        return False
