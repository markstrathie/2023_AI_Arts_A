#!/usr/bin/env python
# coding: utf-8

# # Week 1: Getting started with Anaconda, Jupyter Notebook and Python
# 
# ### Exercises to familiarise myself with Jupyter Notebook and its relationship to Python.
# 
# a) I joined this course because I am interested in the more practical aspects of DMIS. AI can be used as a tool to create and analyse information in many areas.
# 
# b) I have prior experience with Python and a little AI through the computer science classes I took last year.
# 
# c) I expect to learn:
# - how to use AI to help my productivity
# - how to code for machine learning
# - how to combine these into a practical skillset for a future career

# In[1]:


message1 = "Hello, World!"

print (message1[0])


# In[2]:


from IPython.display import *
YouTubeVideo("tK0vp8LlDiM")


# In[ ]:


import webbrowser #importing a library
import requests #importing a library

print("Shall we hunt down an old website?") #printing intro message
site = input("Type a website URL: ") #assigning a value to a variable
era = input("Type year, month, and date, e.g., 20150613: ") #assigning a value to a variable
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era) #assigning a value to a variable
response = requests.get(url) #assigning a value to a variable
data = response.json() #assigning a value to a variable
try:
    old_site = data["archived_snapshots"]["closest"]["url"] #assigning a value to a variable
    print("Found this copy: ", old_site) #printing url of the search result
    print("It should appear in your browser.") #printing message
    webbrowser.open(old_site)
except:
    print("Sorry, could not find the site.") #message to print if no result found


# # Week 2. Exploring Data in Multiple Ways

# In[1]:


from IPython.display import Image

Image ("picture1.jpg")


# In[2]:


from IPython.display import Audio

Audio ("audio1.mid")


# In[3]:


Audio ("GoldbergVariations_MehmetOkonsar-1of3_Var1to10.ogg")

#This file is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported license.
#You are free: 
#•	to share – to copy, distribute and transmit the work
#•	to remix – to adapt the work
#Under the following conditions: 
#•	attribution – You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
#•	share alike – If you remix, transform, or build upon the material, you must distribute your contributions under the same or compatible license as the original.
#The original ogg file was found at the url: 
#https://en.wikipedia.org/wiki/File:GoldbergVariations_MehmetOkonsar-1of3_Var1to10.ogg


# ### Reflections
# 
# The .ogg file plays but the .mid does not. I beleive the file type is not compatible. The library must not have a codec for that file type.

# ## Task 3.2: Using matplotlib

# In[4]:


from matplotlib import pyplot
test_picture = pyplot.imread("picture1.jpg")
print("Numpy array of the image is: ", test_picture)
pyplot.imshow(test_picture)


# In[5]:


test_picture_filtered = 2*test_picture/3
pyplot.imshow(test_picture_filtered)


# ### Discussion
# 
# I believe the RGB colour data is being manipulated by the mutiplication and division.

# ## Task 3-3: Exploring scikit-learn (a.k.a sklearn)

# In[6]:


from sklearn import datasets
dir(datasets)


# ### Dataset choices
# 
# I'm going to look at wine and iris because they sound interesting

# In[7]:


wine_data = datasets.load_wine()
print(wine_data.DESCR)


# In[8]:


wine_data.feature_names


# In[9]:


wine_data.target_names


# In[10]:


wine_data.keys()


# In[11]:


iris_data = datasets.load_iris()
print(iris_data.DESCR)


# In[12]:


from sklearn import datasets
import pandas

wine_data = datasets.load_wine()
wine_dataframe = pandas.DataFrame(data=wine_data['data'], columns = wine_data['feature_names'])
#wine_dataframe.head()
wine_dataframe.describe()


# ### Discussion
# 
# I believe the head() function creates a table with the feature names as column headings.
# The describe() function then populates the row headings and data

# ## Task 3-5: Thinking about data bias
# 
# It is important to consider the data you are using to form your dataset, as bias is almost always present. This can include or leave out variables that cause inaccurate conclusions to be drawn. 5 types:
# 
# - Response or activity bias
#     - Where the majority of data is produce by a minority of the population
#     - Solved by debiasing techniques to improve fairness
# - Selection bias
#      - Non-random subset of items presented to users (popular items at top left)
#      - Solved by randomising choices
# - System drift
#     - System changes that change how user interacts with system (Google adding new recommended searches)
#     - Solved by factoring in these changes
# - Omitted variable
#     - Key variable not recorded
#     - Solved by taking this into account or collecting extra data before processing
# - Societal bias
#     - Data created by humans can often have gender/race stereotypes embedded
#     - Solved by debiasing techniques to improve fairness
#     
# Techniques to correct these depend on the type of bias and can be put in place before, during or after processing the data, which is often then used in AI and machine learning.
# 
# Weighing data to minimise bias and to simulate real-world populations.

# In[ ]:




