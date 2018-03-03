from app import config
from pymongo import MongoClient


class PymongoClient(object):
    def __init__(self, host, db_name, port=27017):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[db_name]


db_client = PymongoClient(config.MONGODB_HOST, config.MONGODB_DB)
