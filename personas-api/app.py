import os
from flask import Flask
from flask_cors import CORS
from services.mongo_database import start_mongo

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.run(port=5000)

if __name__ == '__main__':
    start_mongo()
    create_app()