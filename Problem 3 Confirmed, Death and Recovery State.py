#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


conda install -c conda-forge pystan


# In[ ]:


conda install -c conda-forge fbprophet


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet
import requests
get_ipython().run_line_magic('matplotlib', 'inline')

url = 'https://pomber.github.io/covid19/timeseries.json'
response = requests.request("GET", url)
data = response.json()

ans = input("Enter the name of the country to know how long it took for that country to become a recovery state.\n")
if (ans.lower() == 'usa') or (ans.lower() == 'us') or (ans.lower() == 'states') or (ans.lower() == 'united states of america') or (ans.lower() == 'the united states of america'):
    ans = 'US'
if (ans.lower() == 'uk') or (ans.lower() == 'england'):
    ans = 'United Kingdom'

weeklydata = {}
for countries in data:
    if countries.lower() == ans.lower():
        for day in range(0, len(data[countries])):
            death = data[countries][day]['confirmed']
            date = data[countries][day]['date']
            weeklydata.update({date: death})

correctdata = {}
for key, value in weeklydata.items():
    if value != 0:
        correctdata.update({key: value})
corona_df = pd.DataFrame({'ds': list(correctdata.keys()), 'y': list(correctdata.values())})
print(corona_df)

pro = Prophet(daily_seasonality=True)
pro.fit(corona_df)

future1 = pro.make_future_dataframe(periods=14)
prediction1 = pro.predict(future1)
pro.plot(prediction1)
plt.xlabel('Date')
plt.ylabel('Confirmed')
plt.legend(['Confirmed Predictions'])
print(type(prediction1))
plt.show()


# In[4]:


import requests
import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

url = 'https://pomber.github.io/covid19/timeseries.json'
response = requests.request("GET", url)
data = response.json()
ans = input("Enter the name of the country to know how long it took for that country to become a death state.\n")
if (ans.lower() == 'usa') or (ans.lower() == 'us') or (ans.lower() == 'states') or (ans.lower() == 'united states of america') or (ans.lower() == 'the united states of america'):
    ans = 'US'
if (ans.lower() == 'uk') or (ans.lower() == 'england'):
    ans = 'United Kingdom'
if (ans.lower() == 'china'):
    print("Death State Data is not available for China as worldwide data has been recorded from 22nd January, 2020.")
for countries in data:
    if countries.lower() == ans.lower():
        x = range(0, len(data[countries]))
        for j in x:
            if data[countries][j]['confirmed'] >= 1:
                break
        for i in x:
            if 0 < data[countries][i]['deaths'] == 1:
                days = i-j+1
                print("The number of days taken for " + ans + " to become a death state is " + str(days) + ".")
                break

weeklydata = {}
for countries in data:
    if countries.lower() == ans.lower():
        for day in range(0, len(data[countries])):
            death = data[countries][day]['deaths']
            date = data[countries][day]['date']
            weeklydata.update({date: death})

correctdata = {}
for key, value in weeklydata.items():
    if value != 0:
        correctdata.update({key: value})
corona_df = pd.DataFrame({'ds': list(correctdata.keys()), 'y': list(correctdata.values())})
print(corona_df)

pro = Prophet(daily_seasonality=True)
pro.fit(corona_df)

future1 = pro.make_future_dataframe(periods=14)
prediction1 = pro.predict(future1)
pro.plot(prediction1)
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.legend(['Deaths Predictions'])
print(type(prediction1))
plt.show()


# In[5]:


import requests
import matplotlib.pyplot as plt
import pandas as pd
from fbprophet import Prophet

url = 'https://pomber.github.io/covid19/timeseries.json'
response = requests.request("GET", url)
data = response.json()
ans = input("Enter the name of the country to know how long it took for that country to become a recovery state.\n")
if (ans.lower() == 'usa') or (ans.lower() == 'us') or (ans.lower() == 'states') or (ans.lower() == 'united states of america') or (ans.lower() == 'the united states of america'):
    ans = 'US'
if (ans.lower() == 'uk') or (ans.lower() == 'england'):
    ans = 'United Kingdom'

for countries in data:
    if countries.lower() == ans.lower():
        x = range(0, len(data[countries]))
        for j in x:
            if data[countries][j]['confirmed'] >= 1:
                break
        for i in x:
            if 0 < data[countries][i]['recovered']:
                days = i-j+1
                print("The number of days taken for " + ans + " to become a recovery state is " + str(days) + ".")
            break

weeklydata = {}
for countries in data:
    if countries.lower() == ans.lower():
        for day in range(0, len(data[countries])):
            death = data[countries][day]['recovered']
            date = data[countries][day]['date']
            weeklydata.update({date: death})

correctdata = {}
for key, value in weeklydata.items():
    if value != 0:
        correctdata.update({key: value})
corona_df = pd.DataFrame({'ds': list(correctdata.keys()), 'y': list(correctdata.values())})
print(corona_df)

pro = Prophet(daily_seasonality=True)
pro.fit(corona_df)

future1 = pro.make_future_dataframe(periods=14)
prediction1 = pro.predict(future1)
pro.plot(prediction1)
plt.xlabel('Date')
plt.ylabel('Recovered')
plt.legend(['Recovered Predictions'])
print(type(prediction1))
plt.show()


# In[ ]:




