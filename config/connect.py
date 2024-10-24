

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def connect():
    uri = "mongodb+srv://llm-db-dev:SaSZjXu4L3LcuVTK@llmcluster.begfk.mongodb.net/?retryWrites=true&w=majority&appName=LLMCLUSTER"

    # Create a new client and connect to the server
    # client = MongoClient(uri, server_api=ServerApi('1'))
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(e)
        return False
