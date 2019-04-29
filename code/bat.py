from pymongo import MongoClient
import datetime
import os
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm

# x = os.popen('git status').read()
# if 'working tree clean' in x:
# 	print('All changes commited.')
# else:
# 	print('Files modified. Commit before running.')
# 	return

client = MongoClient()
db = client["brahmin"]
# repo_name = os.popen('basename `git rev-parse --show-toplevel`').read()
# repo_name = repo_name[:-1]
# models = db[repo_name] #collection- repo name
models = db["knn"]

def signal(**kwargs):

	obj = kwargs['object']
	# print(obj)
	del kwargs['object']
	pkl = pickle.dumps(obj) # pickle.loads(obj) to restore
	kwargs['object_pickle'] = pkl

	t = datetime.datetime.now()
	kwargs["date"] = t.strftime("%d-%b-%Y|%T")
	
	print(kwargs)
	models.insert_one(kwargs)
	print('Database updated!')

def runModel(X, y):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0) # rs = 42
	kn = KNeighborsClassifier(n_neighbors=1) #
	kn.fit(X_train,y_train.values.ravel())

	y_pred = kn.predict(X_test)
	confusion_matrix = sm.confusion_matrix(y_test, y_pred)
	accuracy = kn.score(X_test,y_test.values.ravel())

	return accuracy