# -*- coding: utf-8 -*-
"""House_price_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qp6p9HwkgxfKF0ba3OJQDbrrSrYJ_HqE

Importing the dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

"""Importing the Boston Housing Price Dataset"""

from google.colab import files

uploaded = files.upload()

import os

print(os.listdir())

house_price_dataset = pd.read_csv("boston.csv")

print(house_price_dataset)

house_price_dataframe = pd.DataFrame(house_price_dataset)

X = house_price_dataframe.drop(columns=['MEDV'])

X.head()

y = house_price_dataframe['MEDV']

y.head()

##checking the missing values
house_price_dataframe.isnull().sum()

#statistical measures of the dataset
house_price_dataframe.describe()

"""correlation of the dataset"""

correlation = house_price_dataframe.corr()

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

"""spliting the dataframe for training and testing"""

X = house_price_dataframe.drop(columns=['MEDV'])

y = house_price_dataframe['MEDV']

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=2)

print(X_train.shape, X_test.shape)

"""Model Training
XgBoost Regressor
"""

#load the model
model = XGBRegressor()

# training the model
model.fit(X_train,Y_train)

"""Evaluation



"""

pred_data = model.predict(X_train)

# R squared_error
score_1 = metrics.r2_score(Y_train, pred_data)

# Mean absolute error

score_2 = metrics.mean_absolute_error(Y_train, pred_data)

print('R squared_error', score_1)
print('Mean absolute error', score_2)

"""Visualizing the actual price and predicted price"""

plt.scatter(Y_train, pred_data)
plt.xlabel("actual price")
plt.ylabel("predicted price")
plt.show()

"""prediction for test data"""

test_pred = model.predict(X_test)

# R squared_error
score_1 = metrics.r2_score(Y_test, test_pred)

# Mean absolute error

score_2 = metrics.mean_absolute_error(Y_test, test_pred)

print('R squared_error', score_1)
print('Mean absolute error', score_2)

"""visualizing on the test data"""

plt.scatter(Y_test, test_pred)
plt.xlabel("actual price")
plt.ylabel("predicted price")
plt.show()

