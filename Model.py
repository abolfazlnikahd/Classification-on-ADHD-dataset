import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # وزن‌ها و بایاس‌ها را به صورت تصادفی مقداردهی می‌کنیم
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.random.randn(hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.random.randn(output_size)
        self.epochs = []
        self.accuracy_every_epochs = []
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = self.sigmoid(self.final_input)
        return self.final_output
    
    def backward(self, X, y, output, learning_rate):
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)
        
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)
        
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0) * learning_rate
        self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0) * learning_rate
    
    @staticmethod
    def strfloat2float(strfloat:str):
        print(type(float(strfloat)))

    def add_accuracy_every_epochs(self, output_forward, y_train_onehot):
        predicted_classes = np.argmax(output_forward, axis=1)
        true_classes = np.argmax(y_train_onehot, axis=1)
        accuracy = np.mean(predicted_classes == true_classes)
        self.accuracy_every_epochs.append(float(f'{accuracy:.2f}'))

    def train(self, X, y, epochs, learning_rate, show = False):
        for i in range(epochs):
            self.epochs.append(i)
            output = self.forward(X)
            self.add_accuracy_every_epochs(output, y)
            self.backward(X, y, output, learning_rate)


        if show:
            plt.plot(self.epochs, self.accuracy_every_epochs)
            plt.xlabel('epochs')
            plt.ylabel('accuracy')
            plt.show()

    def predict(self, X):
        return self.forward(X)

