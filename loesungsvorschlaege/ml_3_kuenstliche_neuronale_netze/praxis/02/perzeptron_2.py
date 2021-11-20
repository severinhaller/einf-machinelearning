import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

column_names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
iris_data_set = pd.read_csv("iris.csv", names=column_names, header=None)

# Iris-virginica Datensätze aussortieren, damit der Datensatz linear separierbar ist.
# Dies sind die letzten 50 Datensätze.

# Features aus dem Datensatz separat speichern.
# Nur petal-length (index 2) und petal-width (index 3) verwenden
matrix_X = iris_data_set.iloc[0:100, 2:4].values
matrix_X = np.append(matrix_X, np.ones((100, 1)), axis=1)
# Labels aus dem Datensatz separat speichern
vektor_y = iris_data_set.iloc[0:100, 4].values

# Koordinatenform der (Hyper) Ebene:
# 0 = w_1 * petal_length + w_2 * petal_width + w_0 * 1
w_1 = random.random()
w_2 = random.random()
w_0 = random.random()

w = np.array([w_1, w_2, w_0])
L = 0.5
i = 0

for epoche in range(10):
    for i in range(len(matrix_X)):
        x = matrix_X[i]
        # 1. Gewichtete Summe berechnen
        z = np.dot(w, x)
        # 2. Vorhersage machen mit Schwellenwert 0
        if z >= 0:
            predicted_class = "Iris-versicolor"
        else:
            predicted_class = "Iris-setosa"
        # 3. Tatsächliche Klasse ermitteln
        true_class = vektor_y[i]
        # 4. Gewichte anpassen, falls nicht korrekt klassifiziert
        if true_class != predicted_class:
            if predicted_class == "Iris-setosa":
                w = w + L * x
            else:
                w = w - L * x

print("Gewichte:", w)
petal_lengths = np.linspace(0, 7, 100)
petal_widths = (-w[0] * petal_lengths - w[2]) / w[1]
plt.plot(petal_lengths, petal_widths, "-b")
plt.xlim([0, 5.5])
plt.ylim([-5, 5])
# Die ersten 50 Datensätze sind Iris-setosa
plt.scatter(matrix_X[:50, 0], matrix_X[:50, 1], color="red", marker="o", label="Iris-setosa")
plt.scatter(matrix_X[50:100, 0], matrix_X[50:100, 1], color="blue", marker="x", label="Iris-versicolor")
plt.xlabel("petal-length")
plt.ylabel("petal-width")
plt.legend(loc="upper left")
plt.show()
