from .base import db


class User(db.Document):
    _id = db.ObjectIdField(primary_key=True)
    account = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    balance = db.FloatField(default=0, required=True)
    phone_num = db.StringField(required=True, unique=True)
    pets_list = db.ListField()
    meta = {'strict': False}
