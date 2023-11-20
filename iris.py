# -*- coding: utf-8 -*-
"""iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BH8z8ebKFKaaObZUclNNB5M1HaOwVZBw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import accuracy_score

"""DATA PROCESSING"""

#load data from csv file
filepath='/content/IRIS.csv'
iris=pd.read_csv(filepath)

iris

iris.head()

iris.tail()

iris.describe()

iris.shape

iris.info()

iris.isnull().sum()

iris['species'].value_counts()

iris['sepal_width'].hist()

iris['sepal_length'].hist()

iris['petal_width'].hist()

iris['petal_length'].hist()

sns.scatterplot(x=iris['sepal_length'], y=iris['petal_width'], hue=iris['species'])

flower_mapping={'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2}
iris["species"]=iris["species"].map(flower_mapping)

iris

X=iris[['sepal_length','sepal_width','petal_length','petal_width']].values
y=iris[['species']].values

#y = np.nan_to_num(y, nan=np.nanmean(y))

#y = y.ravel()

model= LogisticRegression()
model.fit(X,y)

model.score(X,y).round(2)

actual=y
pred= model.predict(X)

print(metrics.classification_report(actual,pred))

print(metrics.confusion_matrix(actual,pred))

pred = model.predict([[2.6,4.1,5.1,0.3]])
pred