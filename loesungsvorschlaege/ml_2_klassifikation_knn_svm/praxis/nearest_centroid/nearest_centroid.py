import matplotlib.pyplot as plt
import pandas as pd
import sklearn.metrics as met
import sklearn.model_selection as modsel
import sklearn.neighbors as neigh

column_names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
# Lade die Daten aus der CSV-Datei iris.csv in ein Data Frame.
# Verwende die Spaltennamen aus column_names, da die CSV-Datei keine Spaltennamen besitzt.
iris_data_set = pd.read_csv("iris.csv", names=column_names, header=None)
# Gibt die ersten fünf Zeilen des Data Frames aus.
print(iris_data_set.head())
print()
# Gibt die letzten fünf Zeilen des Data Frames aus.
print(iris_data_set.tail())
print()
# Fasse die Daten im Data Frame zusammen (Mittelwert etc.)
print(iris_data_set.describe())
print()

# Die ersten vier Spalten bilden die Features. Wir speichern alle Zeilen in einer Matrix ab.
# 0:150 bedeutet alle Zeile: Zeile mit Index 0 bis und mit Zeile mit Index 149
# 0:4 bedeutet die Spalten mit dem Index 0, 1, 2 und 3
matrix_X = iris_data_set.iloc[0:150, 0:4].values

# Die letzte Spalte beinhaltet die Klassen. Dies ist ein Vektor.
# 0:150 bedeutet alle Zeile: Zeile mit Index 0 bis und mit Zeile mit Index 149
# 4 bedeutet nur Spalte mit Index 4
vektor_y = iris_data_set.iloc[0:150, 4].values

# Teilt das Daten-Set in Trainingsdaten und Testdaten auf.
train_X, test_X, train_y, test_y = modsel.train_test_split(matrix_X, vektor_y, test_size=0.20)

# Nearest Centroid Klassifizierer erstellen
classifier = neigh.NearestCentroid()
# "fit" bedeutet lernen i.e. Samples speichern
classifier.fit(train_X, train_y)

# Benutze die Testdaten fuer die Vorhersagen
pred_y = classifier.predict(test_X)

# Wahrheitsmatrix (Konfusionsmatrix) bestimmen
print(met.confusion_matrix(test_y, pred_y))
print()
# Bestimme Precision, Recal, F1-Score, Support und Accuracy.
print(met.classification_report(test_y, pred_y))
print()
