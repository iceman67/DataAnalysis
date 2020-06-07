#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import matplotlib.pyplot as plt


# 센서 값에 따른 자료특성 변화

# In[39]:


my_url= "April_sensor_data.csv"
#my_url= "April_All.csv"

#data frame
df = pd.read_csv(my_url, parse_dates=['REG_DATE'])


# In[40]:


df.shape


# In[41]:


df.head()


# In[42]:


# index 컬럼 지정 
df = df.set_index("NO", drop = True)

df['weekday'] = df['REG_DATE'].dt.day_name()
print(df.columns)


# In[43]:


df.shape


# In[44]:


df.head(3)


# In[46]:


df_monday = df[df['weekday']=='Monday']
df_monday.tail()


# In[47]:


df_monday = df[df['weekday']=='Monday']
df_tuesday = df[df['weekday']=='Tuesday']
df_wednesday = df[df['weekday']=='Wednesday']
df_thursday = df[df['weekday']=='Thursday']
df_friday = df[df['weekday']=='Friday']

df_saturday = df[df['weekday']=='Saturday']
df_sunday = df[df['weekday']=='Sunday']


# In[53]:


df_sunday.shape


# In[49]:


df_sunday.tail()


# In[54]:



df_workday = pd.concat([df_monday,df_tuesday, df_wednesday, df_thursday, df_friday])
df_weekend = pd.concat([df_saturday,df_sunday])
#df_weekend = pd.concat([df_saturday])


# In[56]:


df_weekend.shape


# In[57]:


df_workday.describe()


# In[58]:


df_weekend.describe()


# In[59]:


df_workday.head()


# ### group by a single column
# df.groupby('column1')

# In[8]:


df.groupby('weekday')


# In[9]:


week_df = df.groupby(df['weekday']).mean()


# In[10]:


week_df


# In[11]:


df.groupby('weekday').groups


# In[12]:


def grouping(week):
    if week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday']:
        return 'Group1'
    else:
        return 'Group2'


# In[13]:


grouping('Sunday')


# In[14]:


df_group = df.groupby(grouping).groups


# In[15]:


df_group = df.groupby('weekday')


# In[18]:


len(df_group)


 


# In[60]:


df_workday = df_workday.rename(columns={'Huminity': 'Humidity', 'PM2.5' :'PM25', 'PM10.0':'PM100'})


# In[61]:


df_weekend = df_weekend.rename(columns={'Huminity': 'Humidity', 'PM2.5' :'PM25', 'PM10.0':'PM100'})


# In[62]:


df_weekend.columns


# In[63]:


fig, axes = plt.subplots(5,2, figsize=(10,20))
x  = list(range(len(df_workday['PM25'])))
axes[0][0].plot(x, df_workday['PM25'])
axes[0][0].set_title ('workday PM2.5')

x1  = list(range(len(df_weekend['PM25'])))
axes[0][1].plot(x1, df_weekend['PM25'])
axes[0][1].set_title ('weekend PM2.5') 


axes[1][0].plot(x, df_workday['Temperature'])
axes[1][0].set_title ('workday Temperature')

axes[1][1].plot(x1, df_weekend['Temperature'])
axes[1][1].set_title ('weekend Temperature') 

axes[2][0].plot(x, df_workday['CO2'])
axes[2][0].set_title ('workday CO2')

axes[2][1].plot(x1, df_weekend['CO2'])
axes[2][1].set_title ('weekend CO2') 

axes[3][0].plot(x, df_workday['Humidity'])
axes[3][0].set_title ('workday Humidity')

axes[3][1].plot(x1, df_weekend['Humidity'])
axes[3][1].set_title ('weekend Humidity') 

axes[4][0].plot(x, df_workday['TVOC'])
axes[4][0].set_title ('workday TVOC')

axes[4][1].plot(x1, df_weekend['TVOC'])
axes[4][1].set_title ('weekend TVOC') 


plt.show()
