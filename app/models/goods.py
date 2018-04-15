from .base import db


class Goods(db.Document):
    _id = db.ObjectIdField()
    name = db.StringField()
    price = db.FloatField()
    label = db.ListField()
    meta = {'strict': False}
