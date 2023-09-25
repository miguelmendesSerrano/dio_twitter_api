from pymongo import MongoClient

URI = "mongodb+srv://dio-twitter-api:dvVTXSvWyniVAHam@cluster0.4bov0n3.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(URI)

db = client.dio_twitter

users_collection = db.users
