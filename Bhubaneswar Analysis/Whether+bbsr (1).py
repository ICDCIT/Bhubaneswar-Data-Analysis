
# coding: utf-8

# In[15]:

#This function is the analysis report of bhubaneswar whether
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.style as style
df = pd.read_csv('PIC_bbsrtemperature.csv')

ac=df['High']
ac
bd=df['Months']
ef=df['Low']
gh=df['Avg']

Y=range(12)

plt.close("all")

plt.figure(figsize=(12,8))
plt.style.use('fivethirtyeight')
plt.plot(Y,ac,marker='.',label='Highest Temp')
ax=plt.subplot()
for i,j in df.High.items():
    ax.annotate(str(j), xy=(i, j))
plt.plot(Y,ef,marker='.',label='Lowest Temp')
for i,j in df.Low.items():
    ax.annotate(str(j), xy=(i, j))

plt.plot(Y,gh,marker='.',label='Average Temp')
for i,j in df.Avg.items():
    ax.annotate(str(j), xy=(i, j))

plt.legend()
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Bhubaneswar 2018 Temperature')

ax.set_xticks(Y)

ax.set_xticklabels(bd,rotation=30,color='navy')


for i,j in df.High.items():
    ax.annotate(str(j), xy=(i, j))

plt.show()



# ### October to March is found to be the best period to travel Bhubaneswar .While June is the hottest month of the year wih 42degree Celcius.April To September is consdered the hottest period of the whole year.

# In[ ]:



