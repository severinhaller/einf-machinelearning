# Beispiel aus dem Skript in Python programmiert
# 3.7 Abstraktes Beispiel
# 3.8 Methode der kleinsten Quadrate
# 3.9 Abstraktes Beispiel
# 3.10 Lösung für die Methode der kleinsten Quadrate

import numpy as np

# Daten als Matrix darstellen: 4 Zeilen und 3 Spalten
# Angabe erfolgt zeilenweise: [10, 1, 1] ist die erste Zeile der Matrix.
matrix_X = np.array([[10, 1, 1], [20, 2, 1], [30, 1, 1], [40, 3, 1]])
print("Matrix X")
print(matrix_X)
print()
# Vektor als "Matrix" mit 4 Zeilen und einer Spalte
vektor_y = np.array([[4], [5], [5], [7]])
print("Vektor y")
print(vektor_y)
print()

# Vektor w bestimmen mit der Methode der kleinsten Quadrate
# w = (X^T * X)^-1 * X^T * y

# 1. Matrix-Matrix-Produkt: transponierte Matrix X mal Matrix X => X^T * X
res_1 = matrix_X.T @ matrix_X
# 2. Inverse der Matrix berechnen => (X^T * X)^-1 = (res_1)^-1
res_2 = np.linalg.inv(res_1)
# 3. Matrix-Matrix-Produkt: transponierte Matrix X mit Ergebnis von (X^T * X)^-1 verrechnen
# => (X^T * X)^-1 * X^T = (res_1)^-1 * X^T = res_2 * X^T
res_3 = res_2 @ matrix_X.T
# 4. Matrix-Vektor-Produkt: Ergebnismatrix mit Vektor y multiplizieren
# => (X^T * X)^-1 * X^T * y = (res_1)^-1 * X^T * y = res_2 * X^T * y = res_3 * y
w = res_3 @ vektor_y
print("Vektor w")
print(w)
