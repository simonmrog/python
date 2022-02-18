import numpy as np
from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = datasets.load_iris()

# train-test splitting
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)
print(model)

# predict
expected = y_test
predicted = model.predict(X_test)

# metrics
classification_report = metrics.classification_report(expected, predicted)
confusion_matrix = metrics.confusion_matrix(expected, predicted)

print(classification_report, confusion_matrix)

# predicting for last row
result = model.predict_proba(iris.data[-1:])
print("Prediction for last row: {}".format(result))

# persist the model
import pickle
import os

# save model to disk
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/iris_model.pkl"
print("Saving to {}...".format(filename))
pickle.dump(model, open(filename, "wb"))

# load model from disk
loaded_model = pickle.load(open(filename, "rb"))
result = loaded_model.predict_proba(iris.data[-1:])
print("Prediction for last row from pickle: {}".format(result))
