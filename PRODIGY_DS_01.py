#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install pandas matplotlib seaborn


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


df = pd.read_csv('Train.csv')


# In[8]:


print(df.head())


# In[9]:


df_filtered = df[['Age', 'Sex']].dropna()


# In[10]:


df_filtered.columns = ['Age', 'Gender']


# In[11]:


plt.figure(figsize=(10, 6))
sns.histplot(df_filtered['Age'], bins=10, kde=False)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[12]:


plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', data=df_filtered)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[ ]:




