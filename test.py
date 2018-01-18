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

#找到欧氏距离最接近的num个字段
#data_x:读入的x（dataframe）
#data_y:读入的y（dataframe）
#num:最接近的num个字段
num = 3
#def findColName(num, data_x, data_y):
table_x = data_x.loc[:, ["table_name", "column_name"]]
table_y = data_y.loc[:, ["table_name", "column_name"]]
data_x.drop(["table_name", "column_name"], axis=1, inplace=True)
data_y.drop(["table_name", "column_name"], axis=1, inplace=True)
data_y.loc[147:147, :] = 1, 0, 0, 138, 0, 20, 12.57, 157.89
train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.3)
reg = MLPRegressor()
# 直接把train_y中的空值填入train_x中的对应数据
reg.fit(train_x, train_y)
res = reg.predict(test_x)
scaler_x = StandardScaler()
scaler_y = StandardScaler()
scaler_y.fit(test_y)
scaler_x.fit(res)
x = scaler_x.transform(res)
y = scaler_y.transform(test_y)
#遍历预测值
list_all = []
for i in range(0,res.shape[0]):
    list = []
    #遍历实际值
    for j in range(0,test_y.values.shape[0]):
        #计算预测值与实际值的差，将一个预测值与各实际值的差放入list并排序
        len = np.linalg.norm(y[j] - x[i])
        index = test_y.index[j]
        t = (index,len)
        list.append(t)
    list.sort(key=lambda v: v[1])
    list = list[0:num]
    list_name = []
    table_name_x = table_x.at[test_x.index[i],"table_name"]
    column_name_x = table_x.at[test_x.index[i], "column_name"]
    list_name.append(table_name_x + "+" + column_name_x)
    for l in list:
        table_name_y = table_y.at[l[0],"table_name"]
        column_name_y = table_y.at[l[0],"column_name"]
        list_name.append(table_name_y + "+" + column_name_y)
    list_all.append(list_name)
    df_all = pd.DataFrame(list_all)
#    return df_all