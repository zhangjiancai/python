from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import GridSearchCV, train_test_split
import matplotlib.pyplot as plt


def load_data(scale=False):
    data = load_digits()
    x, y = data.data, data.target           ##加载并返回数字数据集
    
    x_train, x_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.3, random_state=10)  ##test_size测试集的大小，如果是小数的话，值在（0,1）之间，表示测试集所占有的比例；如果是整数，表示的是测试集的具体样本数；如果train_size也是None的话，会有一个默认值0.25             random_state这个参数表示随机状态，因为每次分割都是随机的我们希望重复执行的时候，训练集也是一样的
    if scale:
        # ss = StandardScaler()
        ss = MinMaxScaler()                     ##本质上是将数据点映射到了[0,1]区间（默认）
        x_train = ss.fit_transform(x_train)
        x_test = ss.transform(x_test)
    return x_train, x_test, y_train, y_test


def model_selection(x_train, y_train):
    model = KNeighborsClassifier()
    paras = {'n_neighbors': [5, 6, 7, 8, 9, 10], 'p': [1, 2]}
    gs = GridSearchCV(model, paras, verbose=2, cv=5)
    gs.fit(x_train, y_train)
    print('最佳模型:', gs.best_params_, gs.best_score_)


def train(x_train, x_test, y_train, y_test):
    # model = KNeighborsClassifier(5, p=2)
    # model.fit(x_train, y_train)
    # print("Accuracy: ", model.score(x_test, y_test))

    acc = [0]*10
    i = 0
    for k in range(1,11):
        model = KNeighborsClassifier(k, p=2)#表示k-nn算法中选取离测试数据最近的k个点,使用欧式距离进行度量
        model.fit(x_train, y_train)
        acc[i] = model.score(x_test, y_test)##返回给定数据集和标签的平均准确率 
        print("k =", k,", Accuracy: ", acc[i])
        i = i + 1
    
    x=[i+1 for i in range(10)]##循环,查看误差效果
    
    plt.plot(x,acc, marker='o', markersize=5, markerfacecolor='red',markeredgecolor='red', color="black", label='Accuracy of kNN with different k')
    plt.xlabel('k')
    plt.ylabel('Accuracy')
    plt.xticks([1,2,3,4,5,6,7,8,9,10])
    plt.legend()
    plt.show()

if __name__ == '__main__':
    x_train, x_test, y_train, y_test = load_data()
    # model_selection(x_train, y_train)
    train(x_train, x_test, y_train, y_test)
