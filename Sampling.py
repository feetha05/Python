
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns ; sns.set()


# In[8]:


mean_uofm = 155
sd_uofm= 5
mean_gym = 185
sd_gym = 5
gymperc = 0.3
totalPopsize = 4000

# Subgroups
uofm_students = np.random.normal(mean_uofm,sd_uofm, int(totalPopsize*(1-gymperc)))

students_at_gym = np.random.normal(mean_gym,sd_gym, int(totalPopsize*(gymperc)))

population = np.append(uofm_students,students_at_gym)


#set up the figure for plotting

plt.figure(figsize=(10,10))

#plot of U of M Students 
plt.subplot(3,1,1)
sns.distplot(uofm_students)
plt.title("U of M  Students Only")
plt.xlim(140,200)


#plot of Gym Goers 
plt.subplot(3,1,2)
sns.distplot(students_at_gym)
plt.title("Gym Goers")
plt.xlim(140,200)


#plot All Population
plt.subplot(3,1,3)
sns.distplot(population)
plt.title("All Population")
plt.axvline(x = np.mean(population))
plt.xlim(140,200)
plt.show()


# In[9]:


# Sampling from the Entire Population

#Simulation Parameters

numberSamps = 5000
sampSize = 50
# Get the Samping Distribution of the mean for all students 

mean_distribution = np.empty(numberSamps)
for i in range(numberSamps):
    random_students = np.random.choice(population, sampSize)
    mean_distribution[i] = np.mean(random_students)
# plot the Population again
plt.subplot(2,1,1)
sns.distplot(population)
plt.title("Population - II")
plt.axvline(x = np.mean(population))
plt.xlim(140,200)
plt.show()


# In[10]:


# NON REPRESENTATIVE SAMPLE
#Simulation Parameters

numberSamps = 5000
sampSize = 50
# Get the Samping Distribution of the mean for all students 

mean_distribution = np.empty(numberSamps)
for i in range(numberSamps):
    random_students = np.random.choice(students_at_gym, sampSize)
    mean_distribution[i] = np.mean(random_students)
# plot the Population again
plt.subplot(2,1,1)
sns.distplot(population)
plt.title("Population - II")
plt.axvline(x = np.mean(population))
plt.xlim(140,200)
plt.show()

