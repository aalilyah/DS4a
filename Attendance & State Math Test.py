#!/usr/bin/env python
# coding: utf-8

# ## Is there a relationship between attendance and NY State Math Test?

# In[416]:


import pandas as pd
import datetime

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[417]:


attendance = "https://raw.githubusercontent.com/aalilyah/DS4a/Admissions/admissions_2013-2022"
att = pd.read_csv(attendance, index_col = 0)


# In[468]:


math_results = "https://raw.githubusercontent.com/aalilyah/DS4a/main/Math_Results_2015-2022.csv"
results = pd.read_csv(math_results, index_col = 0)


# In[418]:


att['Grade'] = att['Grade'].fillna(0).astype(int)


# In[419]:


att.Year= att.Year.astype(str)
att_clean_year = []

for x in att.Year:
    list1 = x[5:8]
    att_clean_year.append(list1)
    
att['Year'] = att_clean_year


# In[420]:


att.rename(columns = {'% Attendance': 'Attendance'}, inplace = True)


# In[421]:


att = att[(att['Grade']== 6) |(att['Grade']== 7) |(att['Grade']== 8)]
att.Attendance = pd.to_numeric(att.Attendance, errors='coerce')
att = att.dropna(axis = 0)


# In[422]:


att = att.reset_index()


# In[487]:


att.to_csv('attendance')


# In[470]:


results.reset_index(inplace = True)


# In[471]:


results = results[(results['Grade']== '6') |(results['Grade']== '7') |(results['Grade']== '8')]


# In[472]:


results


# In[473]:


results.Year= results.Year.astype(str)
results_clean_year = []

for x in results.Year:
    list1 = x[2:4]
    results_clean_year.append(list1)
    
results.Year = results_clean_year


# In[474]:


#math test clean
results.rename(columns = {'School_DBN': 'DBN'}, inplace = True)


# In[475]:


results


# In[477]:


#columns to str to then merge

att.DBN = att.DBN.astype(str)
results.DBN = results.DBN.astype(str)

att.Year = att.Year.astype(str)
results.Year = results.Year.astype(str)

att.Grade = att.Grade.astype(str)
results.Grade = results.Grade.astype(str)


# In[482]:


test= results.merge(att, how = 'left', on = ['DBN', 'Year', 'Grade'])


# In[486]:


test.to_csv('attendace_corr_statemathtest')


# In[485]:


test


# In[ ]:





# In[ ]:


attvsresults#.groupby(['Grade', 'Year', 'School_Name'])[['Attendance','Percentage_Level_1','Percentage_Level_2',
                                                       #'Percentage_Level_3', 'Percentage_Level_4', 'Percentage_Level_3+4']].mean()


# In[ ]:


#candle cart.. high low or mean.


# In[ ]:


x is year y is district ... then break down by grade level to filter.. 

out of all the district which 

distrcit do over years. do it over all district then compare the district...

line graph to see correlation to see which district vs attendance...


what we are hoping to see as out end product... is the goal to say our data shows these last few years... 
all still do well throughout the years... 

how are each district doing throughtout the year by grade.. 



