import numpy as np
import scipy.special


class NeuralNetwork:
    def __init__(self, number_of_input_nodes, number_of_hidden_nodes, number_of_output_nodes, lernrate):
        self.number_of_input_nodes = number_of_input_nodes
        self.number_of_hidden_nodes = number_of_hidden_nodes
        self.number_of_output_nodes = number_of_output_nodes
        self.lernrate = lernrate

        # Anzahl Zeilen: number_of_hidden_nodes
        # Anzahl Spalten: number_of_input_nodes
        # Bsp. MNIST: 100 x 784 (100 Zeilen und 784 Spalten)

        self.w_input_hidden = np.random.normal(0.0, pow(self.number_of_input_nodes, -0.5),
                                               (self.number_of_hidden_nodes, self.number_of_input_nodes))
        self.w_hidden_output = np.random.normal(0.0, pow(self.number_of_hidden_nodes, -0.5),
                                                (self.number_of_output_nodes, self.number_of_hidden_nodes))

    def train(self, sample_vektor, target_vektor):
        z = self.w_input_hidden @ sample_vektor
        hidden_output = scipy.special.expit(z)
        z = self.w_hidden_output @ hidden_output
        output = scipy.special.expit(z)

        error_output = target_vektor - output
        error_hidden_output = self.w_hidden_output.T @ error_output

        self.w_hidden_output += self.lernrate * np.dot((error_output * output * (1.0 - output)),
                                                       np.transpose(hidden_output))

        self.w_input_hidden = self.w_input_hidden + self.lernrate * np.dot(error_hidden_output + hidden_output * (
                1 - hidden_output), np.transpose(sample_vektor))

    def predict(self, sample_vektor):
        z = self.w_input_hidden @ sample_vektor
        tmp = 1 / (1 + np.exp(-z))
        z = self.w_hidden_output @ tmp
        outputs = 1 / (1 + np.exp(-z))
        index = np.argmax(outputs)
        print(f"Es ist eine {index}")
        return index
