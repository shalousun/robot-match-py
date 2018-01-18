# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import collections
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from vectorClass import Vector
from sklearn.preprocessing import StandardScaler

data_x = pd.read_csv("D:/robot-match-py/data1/data_x.csv")
data_y = pd.read_csv("D:/robot-match-py/data1/data_y.csv")
data_x.rename(columns = {'IsPartOfPrimaryKey':'primary_key'},inplace = True)
table_x = data_x.loc[:, ["table_name", "column_name"]]
table_y = data_y.loc[:, ["table_name", "column_name"]]
data_x.drop(["table_name", "column_name"], axis=1, inplace=True)
data_y.drop(["table_name", "column_name"], axis=1, inplace=True)
data_y.loc[147:147, :] = 1, 0, 0, 138, 0, 20, 12.57, 157.89
#data_x["max"].apply(lambda x : 1.00 / (1 + 1.00 / np.power(1.01, x)), axis = 1)
data_x_discrete = data_x.loc[:,["data_type","nullable","primary_key"]]
data_y_discrete = data_y.loc[:,["data_type","nullable","primary_key"]]
data_x_continuous = data_x.drop(["data_type","nullable","primary_key"],axis=1)
data_y_continuous = data_y.drop(["data_type","nullable","primary_key"],axis=1)
data_x_discrete.data_type = data_x_discrete.data_type.astype('category')
data_y_discrete.data_type = data_y_discrete.data_type.astype('category')
data_x_discrete = pd.get_dummies(data_x_discrete)
data_y_discrete = pd.get_dummies(data_y_discrete)
data_x_discrete.nullable = data_x_discrete.nullable.astype('category')
data_y_discrete.nullable = data_y_discrete.nullable.astype('category')

data_x_continuous = data_x_continuous.apply(lambda x : 2 * (1 / (1 + 1.00 / np.power(1.01, x)) - 0.5), axis = 1)
data_y_continuous = data_y_continuous.apply(lambda x : 2 * (1 / (1 + 1.00 / np.power(1.01, x)) - 0.5), axis = 1)
data_x = pd.merge(data_x_discrete,data_x_continuous,right_index = True,left_index = True)
data_y = pd.merge(data_y_discrete,data_y_continuous,right_index = True,left_index = True)
