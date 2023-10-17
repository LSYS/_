#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install gensim


# In[1]:


import gensim.downloader as api


# In[2]:


model = api.load("word2vec-google-news-300")


# In[ ]:


# poor | poverty | impoverished | disadvantaged | poorest |poverti


# In[12]:


import pandas as pd


# In[15]:


(
    pd.DataFrame(
        model.most_similar(["poverty", "disadvantaged"], topn=100), 
        columns=["similar_to_poverty", "score"])
    .to_csv("words.csv", index=False)
)


# In[ ]:




