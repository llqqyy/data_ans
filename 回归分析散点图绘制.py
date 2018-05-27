# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']#标签显示中文
mpl.rcParams['axes.unicode_minus'] = False#正常显示正负号
data=np.loadtxt('C:/Users/刘青源/Desktop/回归分析数据.txt')#读取数据
data=np.transpose(data)#将数据进行转置，第一行是月份
#print(data)
#进行库存金额-销售额散点图绘制
fig=plt.figure
ax1=plt.subplot(221)
plt.title('库存金额关系')#设置标题
plt.xlabel('库存金额')#设置x轴标签
plt.ylabel('销售额')#设置y轴标签
plt.legend('库存金额')#设置数据标签
x1=data[1,:]
y1=data[4,:]#数据
plt.scatter(x1,y1,c='r',marker='o')#画图
#进行广告投入-销售额散点图绘制
ax1=plt.subplot(222)
plt.title('广告投入关系')#设置标题
plt.xlabel('广告投入')#设置x轴标签
plt.ylabel('销售额')#设置y轴标签
plt.legend('广告投入')#设置数据标签
x1=data[2,:]
y1=data[4,:]#数据
plt.scatter(x1,y1,c='r',marker='o')#画图
#进行员工-销售额散点图绘制
ax1=plt.subplot(223)
plt.title('员工薪酬关系')#设置标题
plt.xlabel('员工薪酬')#设置x轴标签
plt.ylabel('销售额')#设置y轴标签
plt.legend('员工薪酬')#设置数据标签
x1=data[3,:]
y1=data[4,:]#数据
plt.scatter(x1,y1,c='r',marker='o')#画图
plt.show()



