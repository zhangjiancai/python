from operator import index
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import datasets
#import logging
#logging.basicConfig(level=#print)

data = pd.read_csv('iris.csv',header = None ,skiprows= 1  ) # diabetes
print("\n  data:\n ", data) #调试数据。
num_features = 4
X = data.loc[:, 0:num_features] #取数据表。列，行。行为num_features的数值。

index_c1, index_c2, index_c3 = (data.loc[:, num_features] == 0), (data.loc[:, num_features] == 1),(data.loc[:, num_features] == 2) #读取三个列的数据
#print (" index1: \n" , index_c1 ," \n index2:\n  " ,index_c2 ,"\n index3: \n " ,index_c3 )

plt.subplot(1, 2, 1) #画布的制定：1列二行的子区域，选定第一个区域进行画图。
plt.scatter(X.loc[index_c1, 0], X.loc[index_c1, 1],label='class A')
plt.scatter(X.loc[index_c2, 0], X.loc[index_c2, 1],label='class B')
plt.scatter(X.loc[index_c3, 0], X.loc[index_c3, 1],label='class C')
plt.legend()

#所以图形会有两个大表。一个大表会画出原数据，第二个会画出降维后的数据。

model = PCA(n_components=2) #调用skeylearn的decomposition的函数，保留两个特征值。
W = model.fit_transform(X) #拟合数据转化为标准形式 
#H = model.components_
plt.subplot(1, 2, 2)
plt.scatter(W[index_c1, 0], W[index_c1, 1],label='class A')
plt.scatter(W[index_c2, 0], W[index_c2, 1],label='class B')
plt.scatter(W[index_c3, 0], W[index_c3, 1],label='class C')
plt.legend()
plt.show()
#print( "\n  H: \n " ,H)
#print (" \n W: \n  " , W )

