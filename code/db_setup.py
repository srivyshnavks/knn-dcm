from pymongo import MongoClient

client = MongoClient()
db = client["brahmin"]
models = db["eval"] #collection

