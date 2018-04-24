from .base import db


class User(db.Document):
    _id = db.ObjectIdField()
    account = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    balance = db.FloatField(default=0, required=True)
    phone_num = db.StringField(required=True, unique=True)
    pets_list = db.ListField()
    cart = db.ListField()
    meta = {'strict': False}
