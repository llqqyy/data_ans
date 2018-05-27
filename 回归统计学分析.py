import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.api as sm
data = np.loadtxt('C:/Users/刘青源/Desktop/回归分析数据.txt')  #读取数据
#print(data)
x = data[:, 1:4]#注意 选取的是1，2，3列
X=sm.add_constant(x) #为回归分析加入常数项
#print(x)
y = data[:, 4]
model = sm.OLS(y,X)
results = model.fit()
print("回归系数：")
print(results.params)
print("所有统计数据：")
print(results.summary())
xx=np.delete(x,4,0)
xx=np.delete(xx,14,0)
xx=np.delete(xx,10,0)
X2=sm.add_constant(xx)
yy=np.delete(y,4,0)
yy=np.delete(yy,14,0)
yy=np.delete(yy,10,0)
model = sm.OLS(yy,X2)
results = model.fit()
print("2回归系数：")
print(results.params)
print("2所有统计数据：")
print(results.summary())