import pandas as pd


column_names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]

iris_data_set = pd.read_csv("iris.csv", names=column_names, header=None)

print(iris_data_set.head())
print(iris_data_set.tail())
print(iris_data_set.describe())