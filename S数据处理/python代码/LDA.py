import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

data = pd.read_csv('iris.csv', header=None,skiprows= 1) # diabetes
num_features = 4
X = data.loc[:, 0:num_features]

index_c1, index_c2, index_c3 = (data.loc[:, num_features] == 0), (data.loc[:, num_features] == 1),(data.loc[:, num_features] == 2) #同PCA
plt.subplot(1,2,1)
plt.scatter(X.loc[index_c1, 0], X.loc[index_c1, 1],label='class A')
plt.scatter(X.loc[index_c2, 0], X.loc[index_c2, 1],label='class B')
plt.scatter(X.loc[index_c3, 0], X.loc[index_c3, 1],label='class C')
plt.legend()
# plt.show()


model = LinearDiscriminantAnalysis(n_components=2) #调用LDA方法。2个特征值。
W = model.fit_transform(X,data.loc[:, num_features])
plt.subplot(1,2,2)
plt.scatter(W[index_c1, 0], W[index_c1, 1],label='class A')
plt.scatter(W[index_c2, 0], W[index_c2, 1],label='class B')
plt.scatter(W[index_c3, 0], W[index_c3, 1],label='class C')
plt.legend()
plt.show()


