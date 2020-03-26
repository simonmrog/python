import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import FunctionTransformer

np.random.seed(123)
transformer = FunctionTransformer(np.log, validate=True)

data = pd.read_csv("./data.csv")
x = data.day_number.to_numpy().reshape(-1, 1)
y = data.infected.to_numpy()
y_trans = transformer.fit_transform(y.reshape(-1, 1))            # 1
# x_test = x.reshape(-1, 1)
x_test = np.asarray([17]).reshape(-1, 1)
model = LinearRegression().fit(x, y_trans)         # 2
y_fit = model.predict(x_test)
print ("INFECTED PEOPLE:", math.floor(np.exp(y_fit)))
plt.scatter(x, y)
plt.plot(x_test, np.exp(y_fit), "k--", label="Fit")     # 3
plt.title("Exponential Fit")
plt.show()