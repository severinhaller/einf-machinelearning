import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import svm

column_names = ["x1", "x2", "class"]
# Wir müssen die Klassen durch Zahlen ersetzen, damit die Farben einfacher gezeichnet werden können.
abstrakt_data_set = pd.read_csv("abstrakt_plot.csv", names=column_names, header=None)

# Die ersten zwei Spalten bilden die Features. Wir speichern alle Zeilen in einer Matrix ab.
X = abstrakt_data_set.iloc[0:12, 0:2].values
# Die letzte (dritte) Spalte beinhaltet die Klassen. Dies ist ein Vektor.
y = abstrakt_data_set.iloc[0:12, 2].values
# fit the model, don't regularize for illustration purposes
clf = svm.SVC(kernel="linear")
clf.fit(X, y)
print("Parameter für die Hyperebene")
print("w = ", clf.coef_)
print("b = ", clf.intercept_)
print()

plt.scatter(X[:, 0], X[:, 1], c=y)

# plot the decision function
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
ax.contour(
    XX, YY, Z, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"]
)

# plot support vectors
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()
