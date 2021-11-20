import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

column_names = ["breite", "hoehe", "class"]
mr_data_set = pd.read_csv("raupen_marienkaefer.csv", names=column_names, header=None)

# Alle Zeilen der ersten beiden Spalten
matrix_X = mr_data_set.iloc[0:20, 0:2].values

# Plot vorbereiten
figure = plt.figure()
ax = figure.add_subplot(111)
plt.xlim([0, 7])
plt.ylim([0, 7])

# Fuer jede Klasse wird eine Zahl erzeugt. Dadurch kann man automatisch jeder Klasse eine Farbe zuweisen lassen.
classes = dict([(y, x + 1) for x, y in enumerate(sorted({"M", "R"}))])
mr_data_set["class"] = mr_data_set["class"].apply(lambda x: classes[x])
mr_data_set.plot.scatter(x="breite", y="hoehe", c="class", colormap="Set1", ax=ax)

# Startwerte
w_1 = 0
lernrate = 0.5

for i in range(len(matrix_X)):
    # Breite und Länge ermitteln
    breite = matrix_X[i][0]
    laenge = matrix_X[i][1]
    # Länge "vorhersagen"
    y_calc = w_1 * breite
    # Fehler berechnen: Tatsächliche Länge minus "vorhergesagte" Länge.
    error = laenge - y_calc
    # Gewichtsparameter neu bestimmen.
    delta_w = lernrate * (error / breite)
    w_1 = w_1 + delta_w
    # Gerade plotten
    x = np.linspace(0, 4.5, 100)
    y = w_1 * x
    ax.plot(x, y, '-b', label=f'y={w_1}*x')
    plt.pause(1)
    ax.lines = []

plt.show()
