# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('C:/Users/刘青源/Desktop/回归分析数据.txt')  #读取数据
#print(data)
x = data[:, 1:4]#注意 选取的是1，2，3列
#print(x)
y = data[:, 4]
#print(y)
#建模
from sklearn.linear_model import LinearRegression
lrModel = LinearRegression()
#训练模型
lrModel.fit(x, y)
#查看参数
coef=lrModel.coef_
#查看截距
lrModel.intercept_
#预测
pred=lrModel.predict([[150,45,27]])
print('预测销售额为 %f' %(pred))
print("回归系数：")
print (lrModel.coef_)
print("截距：")
print (lrModel.intercept_)
print("拟合判定系数：")
print(lrModel.score(x,y))

