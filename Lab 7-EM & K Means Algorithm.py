import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd 
import numpy as np

np.random.seed(2)       
iris=load_iris() 
x=pd.DataFrame(iris.data)
y=pd.DataFrame(iris.target)
colormap=np.array(['red','blue','green'])

from sklearn.cluster import KMeans 
kmeans=KMeans(n_clusters=3).fit(x) 
plt.subplot(1,2,2) 
plt.title("KMeans") 
plt.scatter(x[2],x[3],c=colormap[kmeans.labels_])
KM_Cluster=kmeans.predict(x)

import sklearn.metrics as sm 
print('K Means Accuracy:',sm.accuracy_score(y,KM_Cluster)) 
print('Confusion Matrix for KMeans:\n',sm.confusion_matrix(y,KM_Cluster))

from sklearn.mixture import GaussianMixture     
gm=GaussianMixture(n_components=3).fit(x) 
ycluster=gm.predict(x) 

plt.subplot(1,2,1) 
plt.title("EM") 
plt.scatter(x[2],x[3],c=colormap[ycluster]) 
print('EM Accuracy:',sm.accuracy_score(y,ycluster)) 
print('Confusion Matrix for EM:\n',sm.confusion_matrix(y,ycluster))

