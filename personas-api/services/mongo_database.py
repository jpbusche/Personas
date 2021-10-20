from mongoengine import connect
from settings import MONGO_URL

class MongoDatabase():

    class MongoInstance():
        def __init__(self, mongo_host):
            connect(host=mongo_host)

    started = False
    def __init__(self, mongo_host):
        if not self.started:
            self.MongoInstance(mongo_host)
            self.started = True

def start_mongo():
    MongoDatabase(MONGO_URL)
