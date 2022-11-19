from math import log 
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

# 运行结果
# 0.9709505944546686
