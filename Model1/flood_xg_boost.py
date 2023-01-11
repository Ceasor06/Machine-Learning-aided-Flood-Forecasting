# -*- coding: utf-8 -*-
"""Flood xg_boost.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dz4j6nAZXNU07cZ3udIoo640fXKm1ZDt

# XGBoost

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('/content/FINAL FINAL FINAL FINAL DATASET WITH DATES.csv',index_col='Date', parse_dates=True)
dataset.index.freq="MS"
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

X

"""## Training XGBoost on the Training set"""

from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)

"""## Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

"""## Plotting output"""

import matplotlib.pyplot as plt
F = np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1)
plt.plot(F[:,0], label="Actual")
plt.plot(F[:,1], label="Pred")
plt.legend()
plt.rcParams['figure.figsize'] = (10, 7)
plt.show()
