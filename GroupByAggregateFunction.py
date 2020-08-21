#!/usr/bin/env python
# coding: utf-8

# #  Group By : Using Agreegate Function with

# # Example

# In[ ]:


df.groupby('variable').agg({'census2010pop': np.average})

