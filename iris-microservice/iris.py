from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":

    iris = datasets.load_iris()

    df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
    df_iris["target"] = pd.Series(iris.target)
    print(df_iris)

    # plotting data
    X = iris.data
    y = iris.target
    colors = [["green", "orange", "blue"][i] for i in y]

    plt.subplot(121)
    plt.scatter(X[:, 0], X[:, 1], c=colors)
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])

    plt.subplot(122)
    plt.scatter(X[:, 2], X[:, 3], c=colors)
    plt.xlabel(iris.feature_names[2])
    plt.ylabel(iris.feature_names[3])

    plt.show()
