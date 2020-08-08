
# coding: utf-8

# In[1]:


# Emipirical Rule of Distribution
import warnings
warnings.filterwarnings('ignore')
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#set random seed
random.seed(1738)


# In[2]:


mu = 7 
sigma = 1.7

Observations = [random.normalvariate(mu,sigma) for i in range(100000)]


# In[6]:


# plot distribution in seaborn
sns.distplot(Observations)
plt.axvline(np.mean(Observations)+np.std(Observations),color ='g')
plt.axvline(np.mean(Observations)-np.std(Observations),color ='g')
plt.axvline(np.mean(Observations)+2*np.std(Observations),color ='y')
plt.axvline(np.mean(Observations)-2*np.std(Observations),color ='y')
plt.axvline(np.mean(Observations)+3*np.std(Observations),color ='b')
plt.axvline(np.mean(Observations)-3*np.std(Observations),color ='b')


# In[7]:


# Summary Statistics
# We use a Pandas  Seris Object because it allows us to use the  describe function
pd.Series(Observations).describe()    


# In[12]:


# Pull 3 Random Samples
SampleA = random.sample(Observations,100)
SampleB =  random.sample(Observations,100)
SampleC =  random.sample(Observations,100)


# In[13]:


#Overlay three Samples A,B,C
fig , ax = plt.subplots() #  Allows us to overlay distributions of Samples A, B and C

sns.distplot(SampleA, ax=ax)
sns.distplot(SampleB, ax=ax)
sns.distplot(SampleC, ax=ax)


# In[19]:


# Construction of Emipirical Cummulative Density Function
from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt
ecdf = ECDF(Observations)
ecdf.x 
plt.plot(ecdf.x,ecdf.y)
#Create horizontal  Line
plt.axhline(y=0.025,color ='y',linestyle='-')
plt.axvline(x = np.mean(Observations)-(2*np.std(Observations)), color = 'y', linestyle='-')

plt.axhline(y=0.975,color ='y',linestyle='-')
plt.axvline(x = np.mean(Observations)+(2*np.std(Observations)), color = 'y', linestyle='-')

