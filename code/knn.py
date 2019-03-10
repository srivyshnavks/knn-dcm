import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import sklearn.metrics as sm
import os

iris = pd.read_csv('../data/iris-raw.csv')
X = iris.iloc[:, 1:5]
y = iris.iloc[:, 5:6]

le = LabelEncoder()
y = le.fit_transform(y)

y = pd.DataFrame(y)
y.columns = ['Species']
new_iris = pd.concat([X, y], axis = 1)
new_iris.to_csv('../data/iris-new.csv', index=False)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0) # rs = 42
kn = KNeighborsClassifier(n_neighbors=1) #
kn.fit(X_train,y_train.values.ravel())

y_pred = kn.predict(X_test)
confusion_matrix = sm.confusion_matrix(y_test, y_pred)
accuracy = kn.score(X_test,y_test.values.ravel())
print(accuracy)
print(confusion_matrix)

with open('../model/model1.pkl','wb') as f:
	pickle.dump(kn, f)
