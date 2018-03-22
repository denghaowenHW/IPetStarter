from .base import db


class Goods(db.Document):
    _id = db.ObjectIdField(primary_key=True)
    name = db.StringField()
    price = db.FloatField()
    meta = {'strict': False}