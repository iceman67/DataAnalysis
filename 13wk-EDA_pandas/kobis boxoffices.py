#!/usr/bin/env python
# coding: utf-8

# KOBIS 박스오피스 openAPI 사용하기 
# (XML 요청)

# http://kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do

# ![image.png](attachment:image.png)

# In[1]:


key='dac1451451ff54f43e1f0f59d3356f86'


# ![image.png](attachment:image.png)

# In[2]:


from bs4 import BeautifulSoup
import requests as req
  
    
basic_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?"
mDate=20200401

# key는 http://www.kobis.or.kr/kobisopenapi 에서 발급받아 사용하 
mURL = basic_url + "key=" + key +"&" + 'targetDt='+ str(mDate)


# In[3]:


mURL


# In[4]:


resp = req.get(mURL)


# In[8]:


if resp.status_code == resp.ok:
    print ("성공적으로 데이터를 수집함")


# In[9]:


resp.ok


# In[11]:


soup = BeautifulSoup(resp.content, "xml") 
#soup


# In[12]:


titles = soup.find_all('movieNm')


# In[13]:


for i in range(0, len(titles)):
    print(titles[i].get_text())
    


# KOBIS 박스오피스 openAPI 사용하기 
# (JSON 요청)

# In[14]:


import json
import requests
import pandas as pd


# In[15]:


mDate=20200401
mURL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt='+ str(mDate)


# In[17]:


res = requests.get(mURL)
text = res.text


# In[24]:


movieData = json.loads(text)
movieLen = len(movieData['boxOfficeResult']['dailyBoxOfficeList'])
movieDF = pd.DataFrame()
movieDF = movieDF.append(  {"title":"", "cnt":"", "salesShare": "" }, ignore_index=True, sort=False )


# In[25]:


for i in range(movieLen):
   movieDF.loc[i,"title"]= movieData['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm']
   movieDF.loc[i, "cnt"] = movieData['boxOfficeResult']['dailyBoxOfficeList'][i]['salesAmt']
   movieDF.loc[i, "salesShare"] = float(movieData['boxOfficeResult']['dailyBoxOfficeList'][i]['salesShare'])


# In[20]:


movieDF.head()


# In[28]:


import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
 
font_location = 'C:/Windows/Fonts/H2GTRM.ttf' # For Windows
font_name = fm.FontProperties(fname=font_location).get_name()


plt.rc('font', family=font_name)
plt.rcParams["figure.figsize"] = (20,3) 
plt.title('audience' + '(' + str(mDate) +')') 
plt.bar(movieDF['title'], movieDF['salesShare'], color='b')
plt.show()


# In[27]:


movieDF.to_csv('movie'+str(mDate)+'.csv', index=False)


# In[ ]:




