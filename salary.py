# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:39:46 2021

@author: RAJKUMAR POLOJU
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import os
os.chdir("F:\Flask")
dataset = pd.read_csv('salary.csv')
 
X = dataset.iloc[:, :1]
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1]]))
