def minkowskidistance(x,y,p):       #闵可夫斯基距离
    import math
    import numpy as np 
    zipped_coordinate = zip(x,y)
    return math.pow(np.sum([math.pow(np.abs(i[0]-i[1]),p) for i in zipped_coordinate]) , 1/p)

def manhattandistance(x,y):         #曼哈顿距离
    import numpy as np
    x = np.array(x)
    y = np.array(y)
    return np.sum(np.abs(x-y))

def euclideandistance(x,y):         #欧式距离
    import numpy as np 
    x = np.array(x)
    y = np.array(y)
    return np.sqrt(np.sum(np.square(x-y)))

def ChebyshevDistance(x, y):        #切比雪夫距离
    import numpy as np
    x = np.array(x)
    y = np.array(y)
    return np.max(np.abs(x-y))

def CosineDistance(x, y):           #余弦相似度
    import numpy as np
    x = np.array(x)
    y = np.array(y)
    return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

def JaccardDistance(x, y):          #杰卡德相似系数

    import numpy as np

    x=np.asarray(x, np.int32)
    y=np.asarray(y, np.int32)
    return np.double(np.bitwise_and((x!=y).sum())/np.double(np.bitwise_or(x!=0, y!=0).sum()))
    

def HammingDistance(x, y):          #汉明距离
    return sum(x_ch != y_ch for x_ch, y_ch in zip(x, y))
