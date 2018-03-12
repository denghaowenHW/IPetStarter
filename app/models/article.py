from .base import db


class Article(db.Document):
    _id = db.ObjectIdField()
    title = db.StringField()
    author = db.StringField()
    content = db.StringField()
    point_praise_user_list = db.ListField()
    comment_list = db.ListField()
    meta = {'strict': False}