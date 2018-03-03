from .base import db


class User(db.Document):

    meta = {'strict': False}
