import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
lrModel = LinearRegression()
data = np.loadtxt('C:/Users/刘青源/Desktop/回归分析数据.txt')  #读取数据
#print(data)
x = data[:, 1:4]#注意 选取的是1，2，3列
y = data[:, 4]
xx=np.delete(x,4,0)
xx=np.delete(xx,14,0)
xx=np.delete(xx,10,0)
yy=np.delete(y,4,0)
yy=np.delete(yy,14,0)
yy=np.delete(yy,10,0)

lrModel.fit(x, y)
print("1拟合判定系数：")
print(lrModel.score(x,y))
fig=plt.figure
month= data[:,0]
plt.plot(month,y,'k.')
y2=lrModel.predict(x)
plt.plot(month,y2,'g-')
for idx,x in enumerate(month):
    plt.plot([x,x],[y[idx],y2[idx]],'r-')
    aaa=abs(y[idx]-y2[idx])
    plt.plot([x,x],[0,aaa],'g-')
plt.show()
lrModel.fit(xx,yy)
print("2拟合判定系数：")
print(lrModel.score(xx,yy))

