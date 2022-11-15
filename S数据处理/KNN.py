import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,\
    classification_report, confusion_matrix
import pylab as pl

dataset = pd.read_csv("knn_data.csv",header=None)
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
print(y.value_counts())

# 划分测试集与训练集
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.20, random_state=5) #x_train 为目标列不含缺失值的数据（不包括目标列） y_train 为不含缺失值的目标列 
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# 训练模型
clf = KNeighborsClassifier(n_neighbors=17)
clf.fit(X_train, y_train)

# 预测
y_pred = clf.predict(X_test)

# 评价模型
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
clf.score(X_test, y_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 误差图
error = []
# Calculating error for K values between 1 and 40
for i in range(1, 41):
    knn = KNeighborsClassifier(n_neighbors=i)
    _ = knn.fit(X_train, y_train)
    y_pred_i = knn.predict(X_test)
    error.append(np.mean(y_pred_i != y_test))
print(error)
plt.figure(figsize=(12, 6))
plt.plot(range(1, 41), error, color='red',
    linestyle='dashed', marker='o',
    markerfacecolor='blue', markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')
plt.figure()

# decision boundary
X=np.array(X_test)
y=np.array(y_pred)
x_min, x_max = X[:,0].min() - 0.1, X[:,0].max() + 0.1
y_min, y_max = X[:,1].min() - 0.1, X[:,1].max() + 0.1
h = 0.02 # step size in the mesh
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

pl.set_cmap(pl.cm.Paired)
pl.pcolormesh(xx, yy, Z)

# 绘制训练点
for i in range(len(X)):
    if y[i] == 0:
        _ = pl.scatter(X[i,0], X[i,1], c='red', marker='o')
    elif y[i] == 1:
        _ = pl.scatter(X[i,0], X[i,1], c='blue', marker='x')
    elif y[i] == 2:
        _ = pl.scatter(X[i,0], X[i,1], c='green', marker='+')
    else:
        _ = pl.scatter(X[i,0], X[i,1], c='magenta', marker='v')

pl.xlabel('Petal length')
pl.ylabel('Petal width')
pl.xlim(xx.min(), xx.max())
pl.ylim(yy.min(), yy.max())
pl.show()