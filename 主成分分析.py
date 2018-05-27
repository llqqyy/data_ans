# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd 
from sklearn.decomposition import PCA
from sklearn import preprocessing #进行数据标准化处理
f = open('C:/Users/刘青源/Desktop/主成分分析数据.csv')
df_data=pd.read_csv(f,sep=',')
data_x=df_data.iloc[:,1:7];
data_y=data_x.T
print('相关系数矩阵：')
r=np.corrcoef(data_y)#求相关系数矩阵
print(r)
data_X=df_data.iloc[:,2:7]
data_X=preprocessing.scale(data_X)#标准化矩阵
data_yy=data_X.T
r=np.corrcoef(data_yy)
r=np.round(r,3)
v,d=np.linalg.eig(r)# v为特征值，d为特征向量
pca = PCA(n_components=5)  
pca.fit(data_X) 
print('各个成分贡献率：')
print(pca.explained_variance_ratio_) 
F=-1*(np.dot(data_X,d[:,0]))#计算主成分得分
print('主成分得分为：')
print(F)
#将城市和得分按列合并
city=df_data.iloc[:,0]
city=city.T
city=city.tolist()
F=F.tolist()
zoo=np.vstack((city,F))
zoo=zoo.T
zoo=zoo[np.lexsort(zoo.T)]
print(zoo[::-1,:])


