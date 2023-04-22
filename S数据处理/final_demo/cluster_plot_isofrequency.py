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

data = np.random.randint(1, 100, 200)
k = 6
d3=pd.qcut(data,k) #要使用的是pandas中的pd.qcut()函数。qcut()函数本身的作用就是对数据进行等频率的划分。
#但是划分的区间没有什么意义

print(d3.value_counts())
cluster_plot(d3, k).show()


'''
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import KBinsDiscretizer

#读取数据

#data=pd.read_csv('iris.csv')
data = np.random.randint(1, 100, 200)
column_headers =list(data.columns.values)

unselected_features=['species','petalwidth','petalwidth'] #将数据里的离散数据先去除掉，这里需要手工选择。也可以不选择这一步，不过会将本来就离散化的数据进行离散化，会导致最后的数据不正确


selected_features=[item for item in column_headers if item not in set(unselected_features)]

print (selected_features)
#data = np.random.randint(1, 100, 200)

#分箱代码
k=5 #设置分箱数
est=KBinsDiscretizer(n_bins=k,encode='ordinal',strategy='quantile')
est.fit(data[selected_features])
Xt=est.transform(data[selected_features])

#将离散化后的数据与之前的离散数据拼起来
dd=pd.DataFrame(Xt,columns=selected_features)
# print(df)
du=data[unselected_features]
df=pd.concat([du,dd],axis=1)
#print(df)

'''