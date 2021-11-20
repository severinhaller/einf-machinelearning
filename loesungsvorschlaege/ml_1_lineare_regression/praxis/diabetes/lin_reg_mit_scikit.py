import numpy as np
import pandas as pd
import sklearn.linear_model as lin

# Die ersten 10 Spalten beinhalten die Features. Die letzte Spalte beinhaltet das Label (Target).
diabetes_data_set = pd.read_csv("diabetes_daten.csv", header=None)

# Matrix X: alle 442 Zeilen und die ersten 10 Spalten => X hat die Dimension 442 x 10
matrix_X = diabetes_data_set.iloc[0:442, 0:10].values
print(f"Dimension Matrix X: {matrix_X.shape}")

# Vektor y: alle 442 Zeilen und nur die letzte Spalte => y hat die Dimension 442 x 1
vektor_y = diabetes_data_set.iloc[0:442, 10].values
print(f"Dimension Vektor y: {vektor_y.shape}")

# Berechne die lineare Regression
# Da wir fit_intercept=True angeben müssen wir keine Spalte mit "1'en" zur Matrix X hinzufügen
# dies wird automatisch erledigt.
regr = lin.LinearRegression(fit_intercept=True)
regr.fit(matrix_X, vektor_y)
# coef beinhaltet die Unbekannten => w-Vektor

# Unterdrückt die wissenschaftliche Notation mit e
# Beispiel: -3.63612242e-02 = -3.63612242+10^-2 = -0.0363612242
np.set_printoptions(suppress=True)

print(f"(w_1, w_2, ..., w_10): {regr.coef_}")
print(f"(w_0): {regr.intercept_}")
