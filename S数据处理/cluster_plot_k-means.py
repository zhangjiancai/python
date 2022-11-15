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

import pandas as pd
import numpy as np
# 聚类离散


from sklearn.cluster import KMeans
data = np.random.randint(1, 100, 200)
data = pd.Series(data)
k=5
kmodel = KMeans(n_clusters=k)
kmodel.fit(data.reshape((len(data), 1)))
c = pd.DataFrame(kmodel.cluster_centers_, columns=list('a')).sort_values(by='a')
# rolling_mean表示移动平均，即用当前值和前2个数值取平均数，
# 由于通过移动平均，会使得第一个数变为空值，因此需要使用.iloc[1:]过滤掉空值。
w = pd.rolling_mean(c, 2).iloc[1:]
w = [0] + list(w['a']) + [data.max()]
d5 = pd.cut(data, w, labels=range(k))

cluster_plot(d5, k).show()
