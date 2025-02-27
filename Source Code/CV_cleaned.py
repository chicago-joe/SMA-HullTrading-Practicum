# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:28:47 2019

@author: Zenith
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn import linear_model
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Ridge, Lasso, ElasticNet, LinearRegression

address = "C:/Users/yz_ze/Documents/GitHub/SMA-HullTrading-Practicum/Data/Cleaned/"

train_x = address + "train_x.txt"
train_y = address + "train_y.txt"
test_x = address + "test_x.txt"
test_y = address + "test_y.txt"

train_x_df = pd.read_csv(train_x,delimiter=",",index_col=0)
train_y_df = pd.read_csv(train_y,delimiter=",",index_col=0,header=None)

test_x_df = pd.read_csv(test_x,delimiter=",",index_col=0)
test_y_df = pd.read_csv(test_y,delimiter=",",index_col=0,header=None)

EN = ElasticNet(alpha = 0.00566,l1_ratio = 0.1111)
EN.fit(train_x_df,train_y_df)
pred_y = EN.predict(test_x_df)

up_dir = 0
down_dir = 0
for i in range(len(pred_y)):
    if ((pred_y[i]>0) and (test_y_df.iloc[i,0]>0)):
        up_dir += 1
    elif ((pred_y[i]<0) and (test_y_df.iloc[i,0]<0)):
        down_dir += 1
    else:
        continue

up_dir_y = 0
down_dir_y = 0
for i in test_y_df.iloc[:,0]:
    if i > 0:
        up_dir_y += 1
    else:
        down_dir_y += 1
    
EN.score(test_x_df,test_y_df)