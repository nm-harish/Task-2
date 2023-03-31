# -*- coding: utf-8 -*-
"""Flight Delay Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qElhEXUohEMqHQwWrbeTqnryjAqWZSTO
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
import imblearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score

dataset = pd.read_csv("flightdata.csv")

dataset.info()

dataset = dataset.drop('Unnamed: 25', axis=1)
dataset.isnull().sum()

dataset = dataset[["FL_NUM","MONTH","DAY_OF_MONTH", "DAY_OF_WEEK", "ORIGIN", "DEST", "CRS_ARR_TIME", "DEP_DEL15","ARR_DEL15"]]
dataset.isnull().sum()

dataset[dataset.isnull().any(axis=1)].head(10)

dataset['DEP_DEL15'].mode()

dataset = dataset.fillna({'ARR_DEL15': 1})
dataset = dataset.fillna({'DEP_DEL15': 0})
dataset.iloc[177:185]

import math

for index, row in dataset.iterrows():
  dataset.loc[index, 'CRS_ARS_TIME'] = math.floor(row['CRS_ARR_TIME']/100)
dataset.head()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dataset['DEST'] = le.fit_transform(dataset['DEST'])
dataset['ORIGIN'] = le.fit_transform(dataset['ORIGIN'])

dataset.head(5)

dataset['ORIGIN'].unique()

dataset = pd.get_dummies(dataset, columns=['ORIGIN', 'DEST'])
dataset.head()
x = dataset.iloc[:, 0:8].values
y = dataset.iloc[:, 8:9].values
x

from sklearn.preprocessing import OneHotEncoder
oh = OneHotEncoder()
z=oh.fit_transform(x[:,4:5]).toarray()
t=oh.fit_transform(x[:,5:6]).toarray()
z

t

x=np.delete(x,[4,5],axis=1)