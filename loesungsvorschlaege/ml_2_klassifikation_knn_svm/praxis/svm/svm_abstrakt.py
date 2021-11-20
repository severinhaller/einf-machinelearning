import numpy as np
import pandas as pd
import sklearn.svm as svm

column_names = ["x1", "x2", "class"]
abstrakt_data_set = pd.read_csv("abstrakt.csv", names=column_names, header=None)
print(abstrakt_data_set.head())
print()
print(abstrakt_data_set.tail())
print()
print(abstrakt_data_set.describe())
print()

# Die ersten zwei Spalten bilden die Features. Wir speichern alle Zeilen in einer Matrix ab.
matrix_X = abstrakt_data_set.iloc[0:12, 0:2].values
# Die letzte (dritte) Spalte beinhaltet die Klassen. Dies ist ein Vektor.
vektor_y = abstrakt_data_set.iloc[0:12, 2].values

svclassifier = svm.SVC(kernel="linear")
svclassifier.fit(matrix_X, vektor_y)
print("Parameter für die Hyperebene")
print("w = ", svclassifier.coef_)
print("b = ", svclassifier.intercept_)
print()
print("Supportvektoren")
print(svclassifier.support_vectors_)
print()
print("Klassifiziere")
x_1 = np.array([[8, 8]])
x_2 = np.array([[14, 14]])
res_1 = svclassifier.predict(x_1)
res_2 = svclassifier.predict(x_2)
print("x_1:")
print(x_1)
print(res_1)
print("x_2")
print(x_2)
print(res_2)
