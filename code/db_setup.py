from pymongo import MongoClient
import datetime

client = MongoClient()
db = client["brahmin"]
models = db["knn"] #collection

def update_db(**kwargs):
	kwargs["date"] = datetime.datetime.utcnow()
	print(kwargs)
	model_id = models.insert_one(kwargs).inserted_id
	# print(model_id)
	print('Database updated!')
