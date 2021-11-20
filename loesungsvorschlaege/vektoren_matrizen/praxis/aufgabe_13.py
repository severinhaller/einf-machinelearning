# Abschnitt 3 Aufgaben
# Aufgabe 13
import numpy as np

# Vektor erstellen
print("Vektor erstellen")
vektor_a = np.array([5, 0, -1, 2])
print("Vektor:")
print(vektor_a)
print("Dimension (shape):", vektor_a.shape)
print()

# Spaltenvektor erstellen
print("Spaltenvektor erstellen (explizit)")
# 4 Zeilen und eine Spalte erstellen. Es gibt mehrere Möglichkeiten:
# spalten_vektor = vektor_a[:, np.newaxis]
spalten_vektor_a = vektor_a.reshape((4, 1))
print("Spaltenvektor:")
print(spalten_vektor_a)
print("Dimension (shape):", spalten_vektor_a.shape)
print()

# Zeilenvektor erstellen
print("Zeilenvektor erstellen (explizit)")
# 1 Zeile und vier Spalten erstellen. Es gibt mehrere Möglichkeiten:
# zeilen_vektor = vektor_a[np.newaxis, :]
zeilen_vektor_a = vektor_a.reshape((1, 4))
print("Zeilenvektor:")
print(zeilen_vektor_a)
print("Dimension (shape):", zeilen_vektor_a.shape)
print()

# Man muss nicht immer explizit einen Zeilen- oder Spaltenvektor erstellen. NumPy kann auch mit dem "normalen" Array
# als Vektor umgehen und die Rechenoperationen anwenden.

# Norm/Betrag des Vektors a
norm_vektor_a = np.linalg.norm(vektor_a)
print(f"2er Norm Vektor a: {norm_vektor_a}")
print()

vektor_b = np.array([8, 4, 25])
print("Vektor b transponieren")
vektor_b_t = vektor_b.T
print(vektor_b_t)
print()

print("a mit 0,25 multiplizieren")
# NumPy kann direkt die Multiplikation pro Element durchführen.
vektor_a_2 = 0.25 * vektor_a
print(vektor_a_2)
print()

# Skalarprodukt (Dot Product)
vektor_x = np.array([1, 2, 3])
skalarprodukt_x_x = np.dot(vektor_x, vektor_x)
norm_x = np.linalg.norm(vektor_x)
print("Skalarprodukt von x und x:", skalarprodukt_x_x)
print("Norm von x:", norm_x)
print("Quadrierte Norm von x:", norm_x ** 2)
print()

# Matrix mit verschachtelten eckigen Klammern eingeben.
# Zeile für Zeile
matrix_A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]])
print("Matrix A")
print(matrix_A)
print()

# Matrix mal Vektor mit dem @ Operator
# Matrix A mal Vektor a
ergebnis_vektor = matrix_A @ vektor_a
print("Matrix A mal Vektor a")
print(ergebnis_vektor)
print()

# Standardskalarprodukt als Matrix-Vektor-Produkt
vektor_c = np.array([1, 2, 3])
print("Vektor c:")
print(vektor_c)
skalarprodukt_c_b = vektor_c.T @ vektor_b
print("Skalarprodukt von c und b:", skalarprodukt_c_b)
print()

# Matrixmultiplikation, Transponieren und Inverse einer Matrix
matrix_t = np.array([[2, 1], [6, 4]])
matrix_u = np.array([[2, -0.5], [-3, 1]])
print("Matrix T")
print(matrix_t)
print()
print("Matrix U")
print(matrix_u)
print()

print("Matrix T mal Matrix U")
matrix_i = matrix_t @ matrix_u
print(matrix_i)
print()

print("Inverse einer Matrix berechnen")
matrix_t_invers = np.linalg.inv(matrix_t)
print("Matrix T^-1 (Inverse von T)")
# Sollte identisch sein mit Matrix U
print(matrix_t_invers)
print()

# Transponieren einer Matrix erfolgt wie bei einem Vektor
matrix_A_transponiert = matrix_A.T
print("Matrix A transponiert")
print(matrix_A_transponiert)
