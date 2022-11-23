from math import log
import operator
import pickle


def calcShannonEnt(dataSet):
    # 统计数据数量
    numEntries = len(dataSet)
    # 存储每个label出现次数
    label_counts = {}
    # 统计label出现次数
    for featVec in dataSet:
        current_label = featVec[-1]
        if current_label not in label_counts:  # 提取label信息
            label_counts[current_label] = 0  # 如果label未在dict中则加入
        label_counts[current_label] += 1  # label计数

    shannon_ent = 0  # 经验熵
    # 计算经验熵
    for key in label_counts:
        prob = float(label_counts[key]) / numEntries
        shannon_ent -= prob * log(prob, 2)
    return shannon_ent


def splitDataSet(data_set, axis, value):
    ret_dataset = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec.extend(feat_vec[axis + 1:])
            ret_dataset.append(reduced_feat_vec)
    return ret_dataset


def chooseBestFeatureToSplit(dataSet):
    # 特征数量
    num_features = len(dataSet[0]) - 1
    # 计算数据香农熵
    base_entropy = calcShannonEnt(dataSet)
    # 信息增益
    best_info_gain = 0.0
    # 最优特征索引值
    best_feature = -1
    # 遍历所有特征
    for i in range(num_features):
        # 获取dataset第i个特征
        feat_list = [exampel[i] for exampel in dataSet]
        # 创建set集合，元素不可重合
        unique_val = set(feat_list)
        # 经验条件熵
        new_entropy = 0.0
        # 计算信息增益
        for value in unique_val:
            # sub_dataset划分后的子集
            sub_dataset = splitDataSet(dataSet, i, value)
            # 计算子集的概率
            prob = len(sub_dataset) / float(len(dataSet))
            # 计算经验条件熵
            new_entropy += prob * calcShannonEnt(sub_dataset)
        # 信息增益
        info_gain = base_entropy - new_entropy
        # 打印每个特征的信息增益
        print("第%d个特征的信息增益为%.3f" % (i, info_gain))
        # 计算信息增益
        if info_gain > best_info_gain:
            # 更新信息增益
            best_info_gain = info_gain
            # 记录信息增益最大的特征的索引值
            best_feature = i
    print("最优索引值：" + str(best_feature))
    print()
    return best_feature


def majority_cnt(class_list):
    class_count = {}
    # 统计class_list中每个元素出现的次数
    for vote in class_list:
        if vote not in class_count:
            class_count[vote] = 0
            class_count[vote] += 1
        # 根据字典的值降序排列
        sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def creat_tree(dataSet, labels, featLabels):
    # 取分类标签(是否放贷：yes or no)
    class_list = [exampel[-1] for exampel in dataSet]
    # 如果类别完全相同则停止分类
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 遍历完所有特征时返回出现次数最多的类标签
    if len(dataSet[0]) == 1:
        return majority_cnt(class_list)
    # 选择最优特征
    best_feature = chooseBestFeatureToSplit(dataSet)
    # 最优特征的标签
    best_feature_label = labels[best_feature]
    featLabels.append(best_feature_label)
    # 根据最优特征的标签生成树
    my_tree = {best_feature_label: {}}
    # 删除已使用标签
    del(labels[best_feature])
    # 得到训练集中所有最优特征的属性值
    feat_value = [exampel[best_feature] for exampel in dataSet]
    # 去掉重复属性值
    unique_vls = set(feat_value)
    for value in unique_vls:
        my_tree[best_feature_label][value] = creat_tree(splitDataSet(dataSet, best_feature, value), labels, featLabels)
    return my_tree


def get_num_leaves(my_tree):
    num_leaves = 0
    first_str = next(iter(my_tree))
    second_dict = my_tree[first_str]
    for key in second_dict.keys():
        if type(second_dict[key]).__name__ == 'dict':
            num_leaves += get_num_leaves(second_dict[key])
        else:
                num_leaves += 1
    return num_leaves


def get_tree_depth(my_tree):
    max_depth = 0       # 初始化决策树深度
    firsr_str = next(iter(my_tree))     # python3中myTree.keys()返回的是dict_keys,不在是list,所以不能使用myTree.keys()[0]的方法获取结点属性，可以使用list(myTree.keys())[0]
    second_dict = my_tree[firsr_str]    # 获取下一个字典
    for key in second_dict.keys():
        if type(second_dict[key]).__name__ == 'dict':     # 测试该结点是否为字典，如果不是字典，代表此结点为叶子结点
            this_depth = 1 + get_tree_depth(second_dict[key])
        else:
            this_depth = 1
        if this_depth > max_depth:
            max_depth = this_depth      # 更新层数
    return max_depth


def classify(input_tree, feat_labels, test_vec):
    # 获取决策树节点
    first_str = next(iter(input_tree))
    # 下一个字典
    second_dict = input_tree[first_str]
    feat_index = feat_labels.index(first_str)

    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                class_label = classify(second_dict[key], feat_labels, test_vec)
            else:
                class_label = second_dict[key]
    return class_label


def storeTree(input_tree, filename):
    # 存储树
    with open(filename, 'wb') as fw:
        pickle.dump(input_tree, fw)


def grabTree(filename):
    # 读取树
    fr = open(filename, 'rb')
    return pickle.load(fr)


if __name__ == "__main__":
    # 数据集
  #  dataSet = [[0, 0, 0, 0, 'no'],
   #            [0, 0, 0, 1, 'no'],
   #            [0, 1, 0, 1, 'yes'],
   #            [0, 1, 1, 0, 'yes'],
   #            [0, 0, 0, 0, 'no'],
   #            [1, 0, 0, 0, 'no'],
   #           # [1, 0, 0, 0, 'yes'],
   #            [1, 0, 0, 1, 'no'],
   #            [1, 1, 1, 1, 'yes'],
   #            [1, 0, 1, 2, 'yes'],
   #            [1, 0, 1, 2, 'yes'],
   #            [2, 0, 1, 2, 'yes'],
   #            [2, 0, 1, 1, 'yes'],
   #            [2, 1, 0, 1, 'yes'],
   #            [2, 1, 0, 2, 'yes'],
    #           [2, 0, 0, 0, 'no']]
    dataSet = [[ '坏', '是','否','低'],
                [ '好',' 否','是','高'],
                [ '好', '否', '否', '高'],
                [ '坏', '否' ,'否', '低'],
                [ '坏', '否', '是', '高'],
                ['坏', '是', '是', '低'],
                [ '好', '是' ,'是', '低'],
                [ '好', '否', '否', '高'],
                ['坏', '是', '否', '低'],
                [ '好', '否', '是', '高']]
    # 分类属性
    labels = ['天气', '学生放假', '促销', '收入']

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
    testVec = [ '是' ,'是', '是']
    result = classify(myTree, featLabels, testVec)

    if result == '高':
        print('收入高')
    if result == '低':
        print('收入低')

    # 存储树
    storeTree(myTree,'classifierStorage.txt')

    # 读取树
    myTree2 = grabTree('classifierStorage.txt')
    print(myTree2)

    testVec2 = ['是','否']
    result2 = classify(myTree2, featLabels, testVec)
    if result2 == '高':
        print('shuorugao')
    if result2 == '低':
        print('shuorudi')
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
