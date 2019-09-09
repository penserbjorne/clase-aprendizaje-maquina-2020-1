#!/usr/bin/env python
# coding: utf-8

# In[34]:


from id3 import Id3Estimator, export_graphviz
import numpy as np
import graphviz


# In[35]:


feature_names = ["color",
                 "forma",
                 "tamanio"]


# In[36]:


x = np.array([["rojo", "cuadrado", "grande"],
              ["azul", "cuadrado", "grande"],
              ["rojo", "redondo", "pequenio"],
              ["verde", "cuadrado", "pequenio"],
              ["rojo", "redondo", "grande"],
              ["verde", "cuadrado", "grande"]])


# In[37]:


y = np.array(["+",
              "+",
              "-",
              "-",
              "+",
              "-"])


# In[38]:


id3 = Id3Estimator()


# In[39]:


id3.fit(x, y)


# In[40]:


export_graphviz(id3.tree_, 'arbol.dot', feature_names)


# In[41]:


with open("arbol.dot") as f:
    dot_graph = f.read()


# In[43]:


g = graphviz.Source(dot_graph)
g.render()
g.view()


# In[ ]:




