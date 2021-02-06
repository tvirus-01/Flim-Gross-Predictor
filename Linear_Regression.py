#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[26]:


data = pd.read_csv("cost_revenue_clean.csv")


# In[27]:


data.describe()


# In[28]:


X = df(data, columns=['production_budget_usd'])
y = df(data, columns=['worldwide_gross_usd'])


# In[29]:


plt.figure(figsize=(12,6))
plt.scatter(X, y, alpha=0.3)
plt.title("Flim Cost VS Worldwide Rev")
plt.xlabel("Production Budget $")
plt.ylabel("Worldwide Gross $")
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()


# In[33]:


regression = LinearRegression()
regression.fit(X, y)

regression.coef_
# In[ ]:





# In[39]:


plt.figure(figsize=(12,6))
plt.scatter(X, y, alpha=0.3, color="crimson")
plt.plot(X, regression.predict(X), color="#19dc67", linewidth=2)
plt.title("Flim Cost VS Worldwide Rev")
plt.xlabel("Production Budget $")
plt.ylabel("Worldwide Gross $")
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()


# In[40]:


regression.score(X, y)

