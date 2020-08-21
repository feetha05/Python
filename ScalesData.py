#!/usr/bin/env python
# coding: utf-8

#  # Scales in Python

# In[2]:


import pandas as pd


# In[ ]:


s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])

s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)


#  # Cut Data into bins to build interval data

# In[3]:


s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])


pd.cut(s, 3)

# You can also add labels for the sizes [Small < Medium < Large].
pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])


# # Pivot Tables - Means of summarising data

# In[ ]:


df.pivot_table ( vlues = '(kW)', index = 'YEAR',COLUMNS = 'Make', aggfunc = np.mean)

#Another Way 

print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))

# Another Way to see that allows us to see the All Totals

df.pivot_table ( vlues = '(kW)', index = 'YEAR',COLUMNS = 'Make', aggfunc = [np.mean,np.min], Margins = True)

