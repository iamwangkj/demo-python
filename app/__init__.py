from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('config')
app.config["MONGO_URI"] = "mongodb://localhost:27017/python"
mongo = PyMongo(app)

from app import views
