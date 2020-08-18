#!/usr/bin/env python
# coding: utf-8

# # Importing CSV  from the Web

# In[ ]:


# import url retrieve from urllib.request
from urllib.request import urlretrieve
 

# for drawing graphs import matplotlib

import matplotlib.pyplot as plt    
    
# import Pandas 

import pandas as pd

# pull in the url 

url = ('https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv')

# Save the csv File locally : 

urlretrieve(url,'winequality-red.csv')

# Read the file into a Pandas data Frame using the pd.read_scsv nd assign it to the data frame df because a csv file we seperate the data using the ';' seperator
df = pd.read_csv('winequality-red.csv', sep=';')

# print the head to get the first 5 rows of data 
print(df.head())


# # Summarize the Data

# In[ ]:


# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()


# In[ ]:




