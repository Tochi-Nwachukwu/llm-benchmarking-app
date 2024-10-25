from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import settings


def connect():
    uri = settings.DATABASE_URL
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(e)
        return False
