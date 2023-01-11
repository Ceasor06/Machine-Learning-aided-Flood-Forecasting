# -*- coding: utf-8 -*-
"""AnnFinalFinal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UsRti9HsPpsUe_4cKToZ5cqFsTOrKRuk

Importing Libraries
"""

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

"""Loading datasets"""

dataset = pd.read_csv('/content/why.csv',index_col='Date', parse_dates=True)
dataset.index.freq="MS"
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

print(y)

# from statsmodels.tsa.seasonal import seasonal_decompose
# results = seasonal_decompose(dataset["Flood"])
# results.plot()

"""Splitting the dataset into test and train"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""Normalizing the dataset"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""Adding ANN layers and hidden layers"""

ann = tf.keras.models.Sequential()

ann.add(tf.keras.layers.Dense(units=10, activation='relu'))

ann.add(tf.keras.layers.Dense(units=10, activation='relu'))

ann.add(tf.keras.layers.Dense(units=10, activation='relu'))

ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

ann.fit(X_train, y_train, batch_size = 4, epochs = 1000)

"""Results"""

loss_per_epoch = ann.history.history['loss']
plt.plot(range(len(loss_per_epoch)),loss_per_epoch)

y_pred = ann.predict(X_test)
y_pred = (y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)
