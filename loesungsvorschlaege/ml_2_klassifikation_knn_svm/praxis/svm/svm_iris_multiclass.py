import matplotlib.pyplot as plt
import pandas as pd
import sklearn.metrics as met
import sklearn.model_selection as modsel
import sklearn.svm as svm

column_names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
iris_data_set = pd.read_csv("iris.csv", names=column_names, header=None)
matrix_X = iris_data_set.iloc[0:150, 0:4].values
vektor_y = iris_data_set.iloc[0:150, 4].values

accuracies = []
for i in range(50):
    # Teilt das Daten-Set in Trainingsdaten und Testdaten auf.
    train_X, test_X, train_y, test_y = modsel.train_test_split(matrix_X, vektor_y, test_size=0.20)

    svclassifier = svm.LinearSVC(max_iter=10000)
    svclassifier.fit(matrix_X, vektor_y)
    pred_y = svclassifier.predict(test_X)

    accuracy = met.accuracy_score(test_y, pred_y)
    accuracies.append(accuracy)

plt.figure(figsize=(12, 6))
plt.plot(range(50), accuracies, color="blue", linestyle="dashed", marker="o",
         markerfacecolor="blue", markersize=10)
plt.xlabel("Run")
plt.ylabel("Accuracy")
plt.show()
