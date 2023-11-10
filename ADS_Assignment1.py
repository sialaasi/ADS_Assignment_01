#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('gas.csv')
plt.figure(figsize = (8,5))
plt.plot(df.Year, df.Mexico, 'b.-', label = 'Mexico')
plt.plot(df.Year, df.USA,'g.-', label = 'USA')
plt.plot(df.Year, df['Japan'],'r.-', label  = 'Japan')
plt.title('Gas Prices Overtime in US Dollor')
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.savefig('df_plot.png')
plt.show()
        


# In[93]:


df1 = pd.read_csv('election.csv')
x = df1['state']
y = df1['votes']
plt.legend()
plt.scatter(x, y)
plt.xlabel('States of USA')
plt.ylabel('Total casted Votes')
plt.savefig('df1_plot.png')
plt.show()


# In[92]:


#Population of Pakistan in Survey of 2023
total = 245000000
adult_men = 95000000
adult_women = 115000000
children = 35000000
percentage_men = (adult_men / total) * 100
percentage_women = (adult_women / total) * 100
percentage_children = (children / total_population) * 100

labels = ['Men', 'Women', 'Children']
sizes = [percentage_men, percentage_women, percentage_children]
colors = ['blue', 'coral', 'green']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=120)

plt.axis('equal')
plt.title('Survey of Population in Pakistan')
plt.savefig('df2_plot.png')
plt.show()


# In[ ]:




