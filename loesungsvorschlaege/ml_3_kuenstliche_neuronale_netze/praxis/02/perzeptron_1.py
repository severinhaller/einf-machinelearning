import random

import matplotlib.pyplot as plt
import matplotlib.widgets as wid
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
# Labels durch Zahlen ersetzen: Iris-setosa = -1 und Iris-versicolor = 1
vektor_y = np.where(vektor_y == "Iris-setosa", -1, 1)

# Plot init
fig, ax = plt.subplots(figsize=(8, 5))


# Datensätze plotten
def clear(event):
    ax.clear()
    plt.sca(ax)
    plt.xlim([0, 5.5])
    plt.ylim([-5, 5])
    # Die ersten 50 Datensätze sind Iris-setosa
    ax.scatter(matrix_X[:50, 0], matrix_X[:50, 1], color="red", marker="o", label="Iris-setosa")
    ax.scatter(matrix_X[50:100, 0], matrix_X[50:100, 1], color="blue", marker="x", label="Iris-versicolor")
    plt.xlabel("petal-length")
    plt.ylabel("petal-width")
    plt.legend(loc="upper left")


def update_trennlinie(event):
    global ax
    print("Trennlinie")
    print(w)
    petal_lengths = np.linspace(0, 7, 100)
    petal_widths = (-w[0] * petal_lengths - w[2]) / w[1]
    ax.plot(petal_lengths, petal_widths, "-b")
    plt.draw()


# Koordinatenform der (Hyper) Ebene:
# 0 = w_1 * petal_length + w_2 * petal_width + w_0 * 1
w_1 = random.random()
w_2 = random.random()
w_0 = random.random()

w = np.array([w_1, w_2, w_0])
L = 0.5
i = 0


def trainiere_mit_naechstem_sample(event):
    global w, i
    x = matrix_X[i]
    print("Sample:", i)
    ax.plot(x[0], x[1], "g*")
    plt.draw()
    # 1. Gewichtete Summe berechnen
    z = np.dot(w, x)
    # 2. Vorhersage machen mit Schwellenwert 0
    if z >= 0:
        predicted_class = 1
    else:
        predicted_class = -1
    # 3. Tatsächliche Klasse ermitteln
    true_class = vektor_y[i]
    # 4. Gewichte anpassen, falls nicht korrekt klassifiziert
    if true_class != predicted_class:
        if predicted_class == -1:
            w = w + L * x
        else:
            w = w - L * x
    i = (i + 1) % 100


clear(None)
ax1 = plt.axes([0.6, 0.015, 0.1, 0.05])
button_trennlinie = wid.Button(ax1, "Trennlinie")
button_trennlinie.on_clicked(update_trennlinie)
ax2 = plt.axes([0.75, 0.015, 0.1, 0.05])
button_trainiere = wid.Button(ax2, "Trainiere")
button_trainiere.on_clicked(trainiere_mit_naechstem_sample)
ax3 = plt.axes([0.88, 0.015, 0.1, 0.05])
button_clear = wid.Button(ax3, "Clear")
button_clear.on_clicked(clear)

plt.show()
