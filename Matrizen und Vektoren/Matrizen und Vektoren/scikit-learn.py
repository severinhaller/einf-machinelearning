import sklearn.linear_model as lin
import numpy as np


diabetes_data_set = np.genfromtxt('diabetes_daten.csv', delimiter=',', encoding ="utf_8_sig")

matrix_x = diabetes_data_set[:, :10]

y = diabetes_data_set[:, np.newaxis, 10]


regr = lin.LinearRegression(fit_intercept=False)

regr.fit(matrix_x,y)

print(regr.coef_)