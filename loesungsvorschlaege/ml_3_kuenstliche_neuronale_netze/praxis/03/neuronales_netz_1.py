import numpy as np


def predict(sample):
    matrix_w_input_hidden = np.array([[0.9, 0.3, 0.4], [0.2, 0.8, 0.2], [0.1, 0.5, 0.6]])
    matrix_w_hidden_output = np.array([[0.3, 0.7, 0.5], [0.6, 0.5, 0.2], [0.8, 0.1, 0.9]])
    # Berechnung zwischen Input Layer und Hidden Layer
    # Matrix mal Vektor
    z = matrix_w_input_hidden @ sample
    # Sigmoid berechnen
    # numpy exp: komponentenweise exp berechnen
    tmp = 1 / (1 + np.exp(-z))
    # Berechnung zwischen Hidden Layer und Output Layer
    z = matrix_w_hidden_output @ tmp
    o = 1 / (1 + np.exp(-z))
    # Bestimme den Index des grössten Elements im Vektor
    index = np.argmax(o)
    if index == 0:
        print("Klasse 1")
    elif index == 1:
        print("Klasse 2")
    else:
        print("Klasse 3")


i = np.array([0.9, 0.1, 0.8])
predict(i)
random_vektor = np.random.rand(3, 1)
predict(random_vektor)
