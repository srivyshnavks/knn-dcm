import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import sklearn.metrics as sm
import bat
import os

def dataset():
	iris = pd.read_csv('../data/iris-raw.csv')
	X = iris.iloc[:, 1:5]
	y = iris.iloc[:, 5:6]

	le = LabelEncoder()
	y = le.fit_transform(y)

	y = pd.DataFrame(y)
	y.columns = ['Species']
	new_iris = pd.concat([X, y], axis = 1)
	new_iris.to_csv('../data/iris-new.csv', index=False)
	return X, y

def model(X, y):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42) # rs = 42
	kn = KNeighborsClassifier(n_neighbors=3) #
	kn.fit(X_train,y_train.values.ravel())

	y_pred = kn.predict(X_test)
	confusion_matrix = sm.confusion_matrix(y_test, y_pred)
	accuracy = kn.score(X_test,y_test.values.ravel())
	# print(accuracy)
	# print(confusion_matrix)

	# convert arrays or list to json format before passing
	bat.signal(test_size = 0.30, n_neighbors = 3, random_state = 42,
			   object = kn, accuracy = accuracy) # pass keyword arguments to store in db

	# with open('../model/model1.pkl','wb') as f:
	# 	pickle.dump(kn, f)

if __name__ == '__main__':
	X, y = dataset()
	model(X, y)
