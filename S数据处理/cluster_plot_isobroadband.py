# 可视化
def cluster_plot(d, k):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(12, 4))
    for j in range(0, k):
        plt.plot(data[d == j], [j for i in d[d == j]], 'o')

    plt.ylim(-0.5, k - 0.5)
    return plt

import numpy as np 
import pandas as pd

#data = pd.read_csv('iris.csv',header = None ,skiprows= 1 , ) # diabetes 
#data = data[0] #读取第0列。

data = np.random.randint(1, 100, 200) #随机产生200个数。这些数的范围是1~100
print (data)
k = 5 # 分为5个等宽区间
# 等宽离散
d1 = pd.cut(data, k, labels=range(k)) #这里主要使用的是pandas库中的cut函数。
cluster_plot(d1, k).show()