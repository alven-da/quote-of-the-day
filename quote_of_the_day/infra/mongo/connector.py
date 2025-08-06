from mongoengine import connect
import os

# def init_mongo():
#   mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/statements")
#   connect(host=mongo_uri)

class MongoConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoConnection, cls).__new__(cls)
            cls._instance._init_connection()
        return cls._instance

    def _init_connection(self):
        # (db, host, port)
        connect('quote_of_the_day', host='localhost', port=27017)