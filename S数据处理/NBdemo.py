from sklearn import tree
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
import pandas as pd
data_url = "iris.csv"
df = pd.read_csv(data_url,header = None ,skiprows= 1)
print (df)
x = df.iloc[:, 1:5]
y = df.iloc[:, 4]
print (y)
clf = GaussianNB()
clf = clf.fit(x, y)
print (clf)

data_urltest = "iristest.csv"
dftest = pd.read_csv(data_urltest)
print (dftest)
xtest = dftest.iloc[:, 1:5]

print(clf.predict(xtest))