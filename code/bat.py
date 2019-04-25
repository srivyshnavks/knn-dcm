from pymongo import MongoClient
import datetime

# import os
# x = os.popen('git status').read()
# if 'working tree clean' in x:
# 	print('All changes commited.')
# else:
# 	print('Files modified. Commit before running.')


client = MongoClient()
db = client["brahmin"]
repo_name = os.popen('basename `git rev-parse --show-toplevel`').read()
repo_name = repo_name[:-1]
# models = db[repo_name] #collection- repo name
models = db["knn"]

def signal(**kwargs):
	t = datetime.datetime.now()
	kwargs["date"] = t.strftime("%d-%b-%Y|%T")
	print(kwargs)
	models.insert_one(kwargs)
	print('Database updated!')