#!/usr/bin/env python
# coding: utf-8

# #   HTTP requests in Python using urllib

# In[1]:


# Import packages

from urllib.request import urlopen , Request 

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request

request = Request(url)

# Sends the request and catches the response: response

response = urlopen(request)

html = response.read()

response.close()

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()


# In[ ]:




