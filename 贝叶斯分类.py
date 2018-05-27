import pandas as pd
import numpy as np

f = open('C:/Users/刘青源/Desktop/贝叶斯判断数据.csv')  # 注意!!!当文件名字带有中文的时候，先f open出来，然后在使用pandas
df_data = pd.read_csv(f,
                      sep=',')  # filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
data_x = (df_data.loc[:, ['指标1', '指标2']])
data_y = df_data['类别']
f.closed
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB().fit(data_x, data_y)
pred = clf.predict([[380.20, 9.08]])
print('类别为 %d' % pred)
''''' 
partial_fit说明：增量的训练一批样本 
相当于把数据分块每次只学习增量，从而实现核心和在线学习，这是特别有用的，当数据集很大的时候，不适合在内存中运算 
该方法具有一定的性能和数值稳定性的开销，因此最好是作用在尽可能大的数据块（只要符合内存的预算开销） 

clf_pf = GaussianNB().partial_fit(X, Y, np.unique(Y))  
print clf_pf.predict([[380.20,9.08]])
'''''
