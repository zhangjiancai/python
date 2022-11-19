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
# 测试
testVec = [0, 1, 1, 1]
    result = classify(myTree, featLabels, testVec)

    if result == 'yes':
        print('放贷')
    if result == 'no':
        print('不放贷')
# 运行结果
# 放贷
