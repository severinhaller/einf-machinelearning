import numpy as np
import pandas as pd
import neural_network_mnist

mnist_train = pd.read_csv("mnist_train.csv", header=None)
train_set_size = len(mnist_train.index)
print(train_set_size)
matrix_pixel = mnist_train.iloc[0:train_set_size, 1:785].values
matrix_pixel = (matrix_pixel / 255.0 * 0.99) + 0.01
vektor_ziffern = mnist_train.iloc[0:train_set_size, 0:1].values

knn = neural_network_mnist.NeuralNetwork(784, 200, 10, 0.1)

epochs = 5

for e in range(epochs):
    for i in range(train_set_size):
        sample = matrix_pixel[i, :].reshape((784, 1))
        label = vektor_ziffern[i]
        target = np.zeros(10) + 0.01
        target[label] = 0.99
        target = target.reshape((10, 1))
        knn.train(sample, target)

mnist_test = pd.read_csv("mnist_test.csv", header=None)
test_set_size = len(mnist_test.index)
matrix_pixel = mnist_train.iloc[0:test_set_size, 1:785].values
matrix_pixel = (matrix_pixel / 255.0 * 0.99) + 0.01
vektor_ziffern = mnist_train.iloc[0:test_set_size, 0:1].values

error_counter = 0
for i in range(test_set_size):
    sample = matrix_pixel[i, :].reshape((784, 1))
    predicted_digit = knn.predict(sample)
    label = vektor_ziffern[i]
    if predicted_digit != label:
        error_counter = error_counter + 1
print(f"Number of Errors: {error_counter}")
print(f"Accuracy: {(test_set_size - error_counter) / test_set_size * 100}%")
