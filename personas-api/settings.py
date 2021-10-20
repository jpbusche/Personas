import os
from datetime import timedelta


# Mongo
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
CLUSTER_URL = os.getenv('CLUSTER_URL')
MONGO_URL = f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{CLUSTER_URL}' 

# JWT
SECRET_KEY = os.getenv('SECRET_KEY')
EXPIRATION_TIME = timedelta(days=1)