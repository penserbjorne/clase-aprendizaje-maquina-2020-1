#!/usr/bin/env python
# coding: utf-8

# In[146]:


from sklearn.datasets import load_diabetes
from sklearn.metrics import precision_recall_fscore_support
from sklearn import metrics
from id3 import Id3Estimator, export_graphviz
import numpy as np
import graphviz


# In[147]:


data = load_diabetes()


# In[148]:


size = int(data.data.shape[0]*0.8)
data_t = np.c_[data.data, data.target]


# In[149]:


x_test = data.data[:size, :]
x_train = data.data[size:, :]
y_test = data.target[:size]
y_train = data.target[size:]


# In[150]:


id3 = Id3Estimator()
id3.fit(x_train, y_train)
y_pred = id3.predict(x_test)


# In[151]:


print('Tamaño de test: ',size)
print("Precisión:",metrics.accuracy_score(y_test, y_pred))
print(precision_recall_fscore_support(y_test, y_pred))


# In[152]:


export_graphviz(id3.tree_, 'arbol.dot', data.feature_names)


# In[153]:


with open("arbol.dot") as f:
    dot_graph = f.read()


# In[154]:


g = graphviz.Source(dot_graph)
g.render()
g.view()


# In[ ]:




