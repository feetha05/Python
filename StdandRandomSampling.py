
# coding: utf-8

# In[1]:


# Generating a Seed
import random

random.seed(1234)

random.random()


# In[2]:


# Create Random Distribution 

unifnumbers = [random.uniform(0,1) for i in range(1000)]

unifnumbers


# In[3]:


# General Normal Distribution 
# set your mean and your sigma

mu = 0 
sigma = 1

random.normalvariate(mu,sigma)


# In[4]:


# General Normal Distribution 
# set your mean and your sigma

mu_1 = 5 
sigma_1 = 2

random.normalvariate(mu_1,sigma_1)


# In[5]:


#Create a list of NOrmally  Distributted numbers 
normalnumbers = [random.normalvariate(mu,sigma) for i in range(1000)]
normalnumbers


# In[6]:


# 
import numpy as np
import random

mu_1 = 0 
sigma_1 = 1

Population = [random.normalvariate(mu,sigma) for i in range(10000)]


# In[8]:


#create Two Samples
SampleA = random.sample(Population,500)
SampleB = random.sample(Population,500)


# In[9]:


np.mean(SampleA)


# In[10]:


np.std(SampleA)


# In[12]:




np.std(SampleB)


# In[13]:


np.mean(SampleB )


# In[15]:


#Create  Mean for 100 Random Samples
means = [np.mean(random.sample(Population,100)) for i in range(100)]


# In[17]:


means
np.mean(means)


# In[19]:


#Create  std Dev for 100 Random Samples
standev = [np.std(random.sample(Population,100)) for i in range(100)]
np.std(standev)

