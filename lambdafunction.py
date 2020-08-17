#!/usr/bin/env python
# coding: utf-8

# # Map and Filter Functions Using Lambda Function

# In[1]:


#Example of  Lambda Function to make first two letters a sting into caps
abbrevs = ["usa","esp","chn","jpn","mex","can","rus","rsa"]
abbrevs_upper = list(map(lambda st: st[:2].upper(), abbrevs))
print(abbrevs_upper)


# In[2]:


#Example of  Lambda Function to make all letters in caps
abbrevs = ["usa","esp","chn","jpn","mex","can","rus","rsa"]
abbrevs_upper = list(map(lambda country: country.upper(), abbrevs))
print(abbrevs_upper)


# In[ ]:




