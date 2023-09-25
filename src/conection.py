from pymongo import MongoClient

from src.secret import URI

client = MongoClient(URI)

db = client.dio_twitter

users_collection = db.users
