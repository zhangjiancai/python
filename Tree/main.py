#from 1 import *
#from 2 import *
#from 3 import * 
#from 4 import *
#from 5 import *
#from 6 import *
from bin import *


if __name__ == "__main__":
    # 数据集
    dataSet = [[0, 0, 0, 0, 'no'],
               [0, 0, 0, 1, 'no'],
               [0, 1, 0, 1, 'yes'],
               [0, 1, 1, 0, 'yes'],
               [0, 0, 0, 0, 'no'],
               [1, 0, 0, 0, 'no'],
              # [1, 0, 0, 0, 'yes'],
               [1, 0, 0, 1, 'no'],
               [1, 1, 1, 1, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [2, 0, 1, 2, 'yes'],
               [2, 0, 1, 1, 'yes'],
               [2, 1, 0, 1, 'yes'],
               [2, 1, 0, 2, 'yes'],
               [2, 0, 0, 0, 'no']]
    # 分类属性
    labels = ['年龄', '有工作', '有自己的房子', '信贷情况']

    print(dataSet)
    print()
    print(calcShannonEnt(dataSet))
    print()

    featLabels = []
    myTree = creat_tree(dataSet, labels, featLabels)
    print(myTree)
    print(get_tree_depth(myTree))
    print(get_num_leaves(myTree))

    #测试数据
    testVec = [0, 1, 1, 1]
    result = classify(myTree, featLabels, testVec)

    if result == 'yes':
        print('放贷')
    if result == 'no':
        print('不放贷')

    # 存储树
    storeTree(myTree,'classifierStorage.txt')

    # 读取树
    myTree2 = grabTree('classifierStorage.txt')
    print(myTree2)

    testVec2 = [1, 0]
    result2 = classify(myTree2, featLabels, testVec)
    if result2 == 'yes':
        print('放贷')
    if result2 == 'no':
        print('不放贷')
# 运行结果
# [[0, 0, 0, 0, 'no'], [0, 0, 0, 1, 'no'], [0, 1, 0, 1, 'yes'], [0, 1, 1, 0, 'yes'], [0, 0, 0, 0, 'no'], [1, 0, 0, 0, 'no'], [1, 0, 0, 1, 'no'], [1, 1, 1, 1, 'yes'], [1, 0, 1, 2, 'yes'], [1, 0, 1, 2, 'yes'], [2, 0, 1, 2, 'yes'], [2, 0, 1, 1, 'yes'], [2, 1, 0, 1, 'yes'], [2, 1, 0, 2, 'yes'], [2, 0, 0, 0, 'no']]

# 0.9709505944546686

# 第0个特征的信息增益为0.083
# 第1个特征的信息增益为0.324
# 第2个特征的信息增益为0.420
#　第3个特征的信息增益为0.363
# 最优索引值：2

# 第0个特征的信息增益为0.252
# 第1个特征的信息增益为0.918
# 第2个特征的信息增益为0.474
# 最优索引值：1

# {'有自己的房子': {0: {'有工作': {0: 'no', 1: 'yes'}}, 1: 'yes'}}
# 2
# 3
# 放贷
# {'有自己的房子': {0: {'有工作': {0: 'no', 1: 'yes'}}, 1: 'yes'}}
# 放贷
