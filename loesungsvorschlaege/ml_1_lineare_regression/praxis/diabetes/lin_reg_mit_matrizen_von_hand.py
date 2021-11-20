import numpy as np
import pandas as pd

# Die ersten 10 Spalten beinhalten die Features. Die letzte Spalte beinhaltet das Label (Target).
diabetes_data_set = pd.read_csv("diabetes_daten.csv", header=None)

# Matrix X: alle 442 Zeilen und die ersten 10 Spalten => X hat die Dimension 442 x 10
matrix_X = diabetes_data_set.iloc[0:442, 0:10].values
print(f"Dimension Matrix X: {matrix_X.shape}")
# Für das Gewicht w_0 muss eine Spalte mit nur "1'en" hinzugefügt werden.
vektor_ones = np.ones((442, 1))
matrix_X = np.append(matrix_X, vektor_ones, axis=1)
print(f"Dimension Matrix X (neu): {matrix_X.shape}")
print()

# Vektor y: alle 442 Zeilen und nur die letzte Spalte => y hat die Dimension 442 x 1
vektor_y = diabetes_data_set.iloc[0:442, 10].values
print(f"Dimension Vektor y: {vektor_y.shape}")
print()

# Vektor w bestimmen mit der Methode der kleinsten Quadrate
# w = (X^T * X)^-1 * X^T * y

res_1 = matrix_X.T @ matrix_X
res_2 = np.linalg.inv(res_1)
res_3 = res_2 @ matrix_X.T
w = res_3 @ vektor_y
print("Vektor w")
print(f"Dimension: {w.shape}")
print(w)

# Unterdrückt die wissenschaftliche Notation mit e
# Beispiel: -3.63612242e-02 = -3.63612242+10^-2 = -0.0363612242
np.set_printoptions(suppress=True)

# round(w, 4) rundet jeden Eintrag auf 4 Nachkommastellen
print(np.round(w, 4))
