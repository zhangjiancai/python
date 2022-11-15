from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
from sklearn import preprocessing
import csv

#读入数据,用csv来读数据，是专门来读取该文件的，这个方式可以读取各式各样的字符。
Dtree = open(r'All.csv','r')
reader = csv.reader(Dtree)

#获取第一行数据，即为表头。
headers = reader.__next__()

#定义两个列表，保存特征和标签
featureList = []
labelList = []

for row in reader:
    #把label存入List，拿到这一行的最后一个元素
    labelList.append(row[-1])
    rowDict = {}
    #计算了行的长度，除了第一列和标签之外
    for i in range(1,len(row)-1):
        #建立一个数据字典，就是将表头和表头的值相互对应来形成键值对
        rowDict[headers[i]] = row[i]
    #把数据字典存入list
    featureList.append(rowDict)

#把数据转换成01表示
#把所有属性的所有情况写出来，依次排列，0为这种属性没有，1为有
vec = DictVectorizer()
x_data = vec.fit_transform(featureList).toarray()
print("x_data:"+str(x_data))
#打印属性名称
print(vec.get_feature_names())

print("labelList:"+str(labelList))
#把标签换成01表示
lb = preprocessing.LabelBinarizer()
y_data = lb.fit_transform(labelList)
print("y_data:"+str(y_data))

#创建决策树模型,算法使用C4.5entropy
model = tree.DecisionTreeClassifier(criterion='entropy')
#输入要建立的模型
model.fit(x_data,y_data)

#测试
x_test = x_data[0]#选一个样本作为测试数据
print("x_test:"+str(x_test))

predict = model.predict(x_test.reshape(1,-1))#将x_test变成一个二维的数据
print("predict:"+str(predict))


#画图
import graphviz

dot_data = tree.export_graphviz(model,
                                out_file=None,
                                #特征的名字，要设置
                                feature_names = vec.get_feature_names(),
                                class_names=lb.classes_,
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('computer')

