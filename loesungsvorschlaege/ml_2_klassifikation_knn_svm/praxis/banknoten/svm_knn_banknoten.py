import pandas as pd
import sklearn.metrics as met
import sklearn.model_selection as modsel
import sklearn.neighbors as neigh
import sklearn.svm as svm

column_names = ["variance", "skewness", "curtosis", "entropy", "class"]
abstrakt_data_set = pd.read_csv("banknoten.csv", names=column_names, header=None)

matrix_X = abstrakt_data_set.iloc[0:1372, 0:4].values
vektor_y = abstrakt_data_set.iloc[0:1372, 4].values

# Daten-Set in Trainingsdaten und Testdaten aufteilen.
train_X, test_X, train_y, test_y = modsel.train_test_split(matrix_X, vektor_y, test_size=0.20)

# SVM mit den Trainingsdaten trainieren
svclassifier = svm.SVC(kernel="linear")
svclassifier.fit(train_X, train_y)

# KNN mit den Trainingsdaten trainieren
knnclassifier = neigh.KNeighborsClassifier(n_neighbors=3)
knnclassifier.fit(train_X, train_y)

# Vorhersagen mit den Testdaten machen
pred_svm_y = svclassifier.predict(test_X)
pred_knn_y = knnclassifier.predict(test_X)
print("Ergebnis SVM")
print(met.classification_report(test_y, pred_svm_y))
print()
print("Ergebnis KNN")
print(met.classification_report(test_y, pred_knn_y))
