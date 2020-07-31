
# coding: utf-8

# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
#load the data set 
tips_data = sns.load_dataset("tips")


# In[5]:


#print out head of tips data set
tips_data.head(5)


# In[8]:


#describe the data by priting the summary statistics
tips_data.describe()


# In[10]:


#plot a histogram of Total Bill

sns.distplot(tips_data["total_bill"],kde=False).set_title("Histogram Of Total Bill")

plt.show()
#plot a histogram of size

sns.distplot(tips_data["size"],kde=False).set_title("Histogram Of Size")

plt.show()

#plot a histogram of tips

sns.distplot(tips_data["tip"],kde=False).set_title("Histogram Of Tip")

plt.show()


# In[11]:


#plot Two Graphs on the same Graph
sns.distplot(tips_data["total_bill"],kde=False)
sns.distplot(tips_data["size"],kde=False).set_title("Histogram Of Size and Total Bill")
plt.show()


# In[13]:


#plot box plots of Total Bill

sns.boxplot(tips_data["total_bill"]).set_title("Histogram Of Total Bill")

plt.show()
#plot a box plot of size

sns.boxplot(tips_data["size"]).set_title("Histogram Of Size")

plt.show()

#plot a boxplot of tips

sns.boxplot(tips_data["tip"]).set_title("Histogram Of Tip")

plt.show()


# In[15]:


# Create Two Box plots together
#plot box plots of Total Bill

sns.boxplot(tips_data["total_bill"])
sns.boxplot(tips_data["size"]).set_title("Histogram Of Size and Total Bill")

plt.show()


# In[16]:


get_ipython().run_line_magic('pinfo', 'sns.distplot')


# In[18]:


sns.boxplot(x = tips_data["tip"], y = tips_data["smoker"])
plt.show()


# In[22]:


#plot side by side historgrams
a = sns.FacetGrid(tips_data,row="smoker")
a = a.map(plt.hist,"tip")
plt.show()

