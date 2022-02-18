import click
import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


class COVIDModel:
    model: LinearRegression
    degree: int
    data: pd.DataFrame
    X: np.ndarray
    y: np.ndarray
    x_train: np.ndarray
    y_train: np.ndarray
    x_test = np.ndarray
    y_pred: np.ndarray

    def __init__(self, data, split_data=False, degree=3):
        self.model = LinearRegression()
        self.degree = degree
        self.split_data = split_data
        self.data = data
        self.X = data["day_number"].to_numpy()
        self.y = data["deaths"].to_numpy()
        if split_data:
            self.x_train, self.x_test, self.y_train, self.y_test = self._split_data()
        else:
            self.x_train = self.X
            self.x_test = self.X
            self.y_train = self.y
        x_train_poly = self._get_polynomials(self.x_train)
        self._train(x_train_poly, self.y_train)

    # train_test_split
    def _split_data(self):
        return train_test_split(self.X, self.y, test_size=0.2)

    # polynomial features
    def _get_polynomials(self, x):
        poly = PolynomialFeatures(degree=self.degree)
        x_poly = poly.fit_transform(x.reshape(-1, 1))
        return x_poly

    def _train(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def predict(self, x_test=None):
        if not self.split_data:
            self.x_test = x_test
        X = np.array(self.x_test).reshape(-1, 1)
        x_test_poly = self._get_polynomials(X)
        self.y_pred = self.model.predict(x_test_poly)
        return self.y_pred

    def score(self):
        return self.model.score(self._get_polynomials(self.x_train), self.y_train)

    def _plot_results(self):
        plt.scatter(self.x_train, self.y_train, color="green")
        plt.scatter(self.x_test, self.y_pred, color="red")
        plt.plot(self.x_train, self.predict(self.x_train), color="red")
        ## plt.plot(self.x_train, self.y_train, color="green")
        plt.xlabel("Time (days)")
        plt.ylabel("Deaths")
        plt.show()


@click.command()
@click.option("--day", default=0, help="day to predict COVID-19 deaths", type=int)
@click.option(
    "--split", default=False, help="train-test splitting of the data", type=bool
)
@click.option("--degree", default=3, help="degree of the fit polynomial", type=int)
def start(day=0, split=False, degree=3):
    data = pd.read_csv("./deaths.csv")
    # print ("DAYS IN DATABASE: ", len(data))
    if day == 0:
        day = len(data) + 1
    day_to_predict = [day]
    model = COVIDModel(data=data, split_data=split, degree=degree)
    prediction = model.predict(day_to_predict)
    score = model.score()
    # model._plot_results()
    print("DEATHS: ", math.floor(prediction[0]), score)
    return prediction, score


if __name__ == "__main__":
    dths, sscore = start()
