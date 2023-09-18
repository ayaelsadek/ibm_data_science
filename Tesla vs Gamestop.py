#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install nbformat==4.2.0')


# In[2]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[3]:


sym=["tsla","gme"]
yf.download(sym)



# In[4]:


type(yf.download(sym))


# In[80]:


url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
tesla=soup.find_all("tbody")[1]
tesla


# In[87]:


columns=["Date","Revenue_in_million"]
tesla_revenue=pd.DataFrame(columns=columns)
Date=""
Revenue_in_million=""
i=1
for tr in tesla.find_all("tr"):
    i=0
    for td in tr.find_all("td"):
        i=i+1
        if (i==1):
            Date=td.text.replace("\n","")
        if(i==2):
            Revenue_in_million=td.text.replace("\n","")
    if (tr!=""):
        tesla_revenue=tesla_revenue.append(pd.Series([Date,Revenue_in_million],index=columns),ignore_index=True)
tesla_revenue
            


# In[95]:


tesla_revenue["Revenue_in_million"] = tesla_revenue['Revenue_in_million'].str.replace(',|\$',"")
tesla_revenue


# In[113]:


tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue_in_million'] != ""]
tesla_revenue
tesla_revenue.tail()


# In[99]:


url=" https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
gme=soup.find_all("tbody")[1]
gme


# In[101]:


columns=["Date","Revenue_in_million"]
gme_revenue=pd.DataFrame(columns=columns)
Date=""
Revenue_in_million=""
i=1
for tr in gme.find_all("tr"):
    i=0
    for td in tr.find_all("td"):
        i=i+1
        if (i==1):
            Date=td.text.replace("\n","")
        if(i==2):
            Revenue_in_million=td.text.replace("\n","")
    if (tr!=""):
        gme_revenue=gme_revenue.append(pd.Series([Date,Revenue_in_million],index=columns),ignore_index=True)
gme_revenue
            


# In[ ]:





# In[105]:


gme_revenue["Revenue_in_million"] = gme_revenue['Revenue_in_million'].str.replace(',|\$',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue_in_million'] != ""]
gme_revenue.tail()


# In[137]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue_in_million.astype("float"), name="Revenue_in_million"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[133]:


sym4="GME"
gme=yf.Ticker(sym4)

table=gme.history(period="max",rounding=True)
table.reset_index(inplace=True)
gme_data=table.head()
gme_data


# In[131]:


sym3="TSLA"
tesla=yf.Ticker(sym3)

df3=tesla.history(period="max",rounding=True)
df3.reset_index(inplace=True)

tesla_data=df3.head()
tesla_data


# In[138]:


make_graph(tesla_data, tesla_revenue, "TSLA")


# In[139]:


make_graph(gme_data, gme_revenue, "GME")


# In[ ]:




