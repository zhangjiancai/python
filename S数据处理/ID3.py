from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


def load_data(scale=True):
    data = load_wine()
    x, y,feature_names = data.data, data.target,data.feature_names
    x_train, x_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.3,
                         shuffle=True, random_state=20)
    if scale:
        ss = StandardScaler()
        x_train = ss.fit_transform(x_train)
        x_test = ss.transform(x_test)
    return x_train, x_test, y_train, y_test,feature_names
##同KNN算法

def train(x_train, x_test, y_train, y_test):
    model = DecisionTreeClassifier(criterion="entropy",max_depth=3)##criterion ： gini或者entropy,前者是基尼系数，后者是信息熵；max_depth设置决策随机森林中的决策树的最大深度，深度越大，越容易过拟合，推荐树的深度为：5-20之间；
    # model = DecisionTreeClassifier(criterion="gini",max_depth=3)
    model.fit(x_train, y_train)
    with open("visualization.dot", "w") as f:
        f = export_graphviz(model, feature_names=feature_names, out_file=f)
    print("Accuracy: ", model.score(x_test, y_test))
    # 决策树可视化
     ##plt.figure()
     ##plot_tree(model, filled=True)
     #plt.title("Decision tree trained on all the wine features")
    # plt.show()

if __name__ == '__main__':
    x_train, x_test, y_train, y_test,feature_names = load_data(False)
    train(x_train, x_test, y_train, y_test)