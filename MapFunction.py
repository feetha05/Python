#!/usr/bin/env python
# coding: utf-8

# In[8]:


people = ['Mr. C Troopz', 'D. Hipgrave Turner']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))


# In[ ]:





# In[ ]:




