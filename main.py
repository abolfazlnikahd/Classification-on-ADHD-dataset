from Resampling import resampling
from Model import NeuralNetwork
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

X_resampled, y_resampled = resampling()

# آماده‌سازی داده‌ها برای آموزش و ارزیابی
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)
#print('--------------------X TRAIN --------------------------')
#print(X_train)
#print('--------------------Y TRAIN --------------------------')
#print(y_train)
#print('--------------------X TEST --------------------------')
#print(X_test)
#print('--------------------Y TEST --------------------------')
#print(y_test)
# تبدیل برچسب‌ها به one-hot encoding
y_train_onehot = pd.get_dummies(y_train).values
#print(y_train_onehot)
y_test_onehot = pd.get_dummies(y_test).values

# ایجاد و آموزش مدل
input_size = X_train.shape[1]
hidden_size = 10  # اندازه لایه مخفی
output_size = y_train_onehot.shape[1]
epochs = 1000
learning_rate = 0.005

nn = NeuralNetwork(input_size, hidden_size, output_size)
nn.train(X_train, y_train_onehot, epochs, learning_rate, show=True)

# پیش‌بینی و ارزیابی
predictions = nn.predict(X_test)
#print(predictions)
predicted_classes = np.argmax(predictions, axis=1)
print(predicted_classes)
true_classes = np.argmax(y_test_onehot, axis=1)
accuracy = np.mean(predicted_classes == true_classes)
print(f'Accuracy: {accuracy:.2f}')
