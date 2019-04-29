import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
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

if __name__ == '__main__':
	X, y = dataset()
	accuracy = bat.runModel(X, y)
	print(accuracy)
