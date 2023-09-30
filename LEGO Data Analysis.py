#!/usr/bin/env python
# coding: utf-8

# # Exploring the evolution of LEGO - Data Analysis

# Lego is a household name across the world, supported by a diverse toy line, hit movies, and a series of successful video games. In this project, we are going to explore a key development in the history of Lego: the introduction of licensed sets such as Star Wars, Super Heroes, and Harry Potter. The two datasets I will be using are shown below:

# ![Screenshot%202023-09-29%20125436.png](attachment:Screenshot%202023-09-29%20125436.png)

# ### Importing libraries

# In[66]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ### Importing the data

# In[22]:


sets=pd.read_csv(r"C:\Users\rache\OneDrive\Desktop\Projects\Python\LEGO data\lego_sets.csv")
sets.head(10)


# In[24]:


themes = pd.read_csv(r"C:\Users\rache\OneDrive\Desktop\Projects\Python\LEGO data\parent_themes.csv")
themes.head(10)


# #### Check Datatype of Each Column

# In[28]:


sets.dtypes


# In[29]:


themes.dtypes


# ### Question 1: What percentage of all licensed sets ever released were Star Wars Themed?

# In[34]:


#lets join the two data sets

merged = sets.merge(themes, left_on = 'parent_theme', right_on = 'name')
merged.drop(columns = 'name_y', inplace=True)
merged.head()


# In[45]:


#getting rid of null values (set_num column)

merged[merged['set_num'].isnull()].shape
merged = merged.dropna(subset='set_num')
merged.head()


# In[46]:


# New data frame with only licensed lego sets
licensed = merged[merged['is_licensed']==True]
licensed.head()


# In[47]:


# data frame with licensed lego sets where the parent theme is 'Star Wars'

star_wars = licensed[licensed['parent_theme']=='Star Wars']
star_wars.head()


# In[53]:


#Now, we want the percentage of Star Wars themed sets that were licensed

star_wars.shape[0]
licensed.shape[0]

the_force = int(star_wars.shape[0]/licensed.shape[0]*100)
print(the_force)

#ANSWER: The percentage of licensed sets that were Star Wars themed is 51%


# In[217]:


#pie chart
counts = licensed.groupby('parent_theme').count()
counts.sort_values('id', ascending=False, inplace=True)
x = counts['id']
#labels= counts[('parent_theme')]
plt.style.use('Solarize_Light2')

counts.plot.pie(y='id', figsize=(10,9), labeldistance=None, title='Licensed Lego Set Themes')
plt.legend(loc="upper right", bbox_to_anchor=(0,1))


# ### Question 2: In which year was Star Wars NOT the most popular licensed theme?

# In[64]:


licensed_sorted = licensed.sort_values('year')
licensed_sorted['count']=1

summed_df = licensed_sorted.groupby(['year','parent_theme']).sum().reset_index()

#Only returning the max count from each year
max_df = summed_df.sort_values('count', ascending=False).drop_duplicates('year')

max_df.sort_values('year')


# In[65]:


year=2017

#ANSWER: The year the Star Wars was NOT the most popular theme was in 2017


# ### Question 3: How many unique sets were released each year (1955-2017)?

# In[233]:


unique_sets = merged
unique_sets.head()
unique_sets['count']=1

sets_per_year = unique_sets.groupby(['year']).sum().reset_index()[['year','count']]
sets_per_year.head(10)


# In[244]:


import seaborn as sns


# In[280]:


year = sets_per_year['year']
count = sets_per_year['count']
count.head()

fig, ax = plt.subplots(figsize=(20, 10))
sns.color_palette("Paired")

sns.barplot(x = 'year',y = 'count',data = sets_per_year, ax=ax, palette=('crest'))

plt.title('Unique Lego Sets per Year')
plt.xlabel('Years')
plt.ylabel('No. of Sets')
fig.autofmt_xdate(rotation=45)


# In[ ]:




