# -*- coding: utf-8 -*-
"""Assignment - 6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BaFc1A7m3AxRUpJz8Vj4ZMbKLrRmbSuS

### 1(b) Given dataset has been uploaded
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv('/content/breastcancer.csv')

df = df.drop(columns=['Unnamed: 32'], errors='ignore')

df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

print(df.head())

"""### 1(a) Added more density layers to the existing code and checked the accurracy level"""

X = df.drop(columns=['id', 'diagnosis'])
y = df['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_task1 = Sequential()
model_task1.add(Dense(32, activation='relu', input_shape=(X_train.shape[1],)))
model_task1.add(Dense(64, activation='relu'))
model_task1.add(Dense(128, activation='relu'))
model_task1.add(Dense(1, activation='sigmoid'))

model_task1.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model_task1.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

accuracy_task1 = model_task1.evaluate(X_test, y_test)[1]
print(f"Task 1 - Model Accuracy: {accuracy_task1}")

"""### 1(c)"""

scaler = StandardScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

model_task3 = Sequential()
model_task3.add(Dense(32, activation='relu', input_shape=(X_train_normalized.shape[1],)))
model_task3.add(Dense(64, activation='relu'))
model_task3.add(Dense(1, activation='sigmoid'))

model_task3.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model_task3.fit(X_train_normalized, y_train, epochs=10, batch_size=32, validation_data=(X_test_normalized, y_test))

accuracy_task3 = model_task3.evaluate(X_test_normalized, y_test)[1]
print(f"Task 3 - Model Accuracy with Normalization: {accuracy_task3}")

"""### 2(a) Plot the loss and accuracy for both training data and validation data using the history object in the source code"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]

history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'], loc='upper right')

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='lower right')

plt.tight_layout()
plt.show()

"""### 2(b) Plot one of the images in the test data, and then do inferencing to check what is the prediction of the model on that single image."""

import numpy as np

index_to_plot = 0
plt.imshow(np.squeeze(test_images[index_to_plot]), cmap='gray')
plt.title(f"True Label: {test_labels[index_to_plot]}")
plt.show()

image_to_predict = test_images[index_to_plot][np.newaxis, ...]
predicted_probabilities = model.predict(image_to_predict)
predicted_label = np.argmax(predicted_probabilities)

print(f"Model Prediction: {predicted_label}")

"""### 2(c) We had used 2 hidden layers and Relu activation. Try to change the number of hidden layer and the activation to tanh or sigmoid and see what happens."""

modified_model = models.Sequential()
modified_model.add(layers.Conv2D(32, (3, 3), activation='tanh', input_shape=(28, 28, 1)))
modified_model.add(layers.MaxPooling2D((2, 2)))
modified_model.add(layers.Conv2D(64, (3, 3), activation='tanh'))
modified_model.add(layers.MaxPooling2D((2, 2)))
modified_model.add(layers.Flatten())
modified_model.add(layers.Dense(128, activation='tanh'))
modified_model.add(layers.Dense(10, activation='softmax'))

modified_model.compile(optimizer='adam',
                       loss='sparse_categorical_crossentropy',
                       metrics=['accuracy'])

modified_history = modified_model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(modified_history.history['loss'])
plt.plot(modified_history.history['val_loss'])
plt.title('Modified Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'], loc='upper right')

plt.subplot(1, 2, 2)
plt.plot(modified_history.history['accuracy'])
plt.plot(modified_history.history['val_accuracy'])
plt.title('Modified Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='lower right')

plt.tight_layout()
plt.show()

"""### 2(d) Run the same code without scaling the images and check the performance."""

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

model_no_scaling = models.Sequential()
model_no_scaling.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model_no_scaling.add(layers.MaxPooling2D((2, 2)))
model_no_scaling.add(layers.Conv2D(64, (3, 3), activation='relu'))
model_no_scaling.add(layers.MaxPooling2D((2, 2)))
model_no_scaling.add(layers.Conv2D(64, (3, 3), activation='relu'))
model_no_scaling.add(layers.Flatten())
model_no_scaling.add(layers.Dense(64, activation='relu'))
model_no_scaling.add(layers.Dense(10, activation='softmax'))

model_no_scaling.compile(optimizer='adam',
                         loss='sparse_categorical_crossentropy',
                         metrics=['accuracy'])

train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]

history_no_scaling = model_no_scaling.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history_no_scaling.history['loss'])
plt.plot(history_no_scaling.history['val_loss'])
plt.title('Model Loss (No Scaling)')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'], loc='upper right')

plt.subplot(1, 2, 2)
plt.plot(history_no_scaling.history['accuracy'])
plt.plot(history_no_scaling.history['val_accuracy'])
plt.title('Model Accuracy (No Scaling)')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'], loc='lower right')

plt.tight_layout()
plt.show()