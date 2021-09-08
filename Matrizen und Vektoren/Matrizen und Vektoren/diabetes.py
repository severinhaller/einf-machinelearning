import numpy as np

diabetes_data_set = np.genfromtxt('diabetes_daten.csv', delimiter=',', encoding="utf_8_sig")
matrix_A = diabetes_data_set[:, :10]
y = diabetes_data_set[:, np.newaxis, 10]

print(matrix_A, y)


w = np.matmul(np.matmul(np.linalg.inv(np.matmul(matrix_A.T, matrix_A)),matrix_A.T),y)

print(w)