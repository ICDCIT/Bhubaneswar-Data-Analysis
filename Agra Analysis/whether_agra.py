
# coding: utf-8

# In[1]:

#This function is the analysis report of agra whether
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.style as style
style.available
df = pd.read_csv('PIC_agratemperature.csv')

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
plt.title('Agra 2018 Temperature')

ax.set_xticks(Y)

ax.set_xticklabels(bd,rotation=30,color='navy')


for i,j in df.High.items():
    ax.annotate(str(j), xy=(i, j))

plt.show()



# In[2]:

#This function is the analysis report of agra whether 
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv('PIC_agratemperature.csv')

ac=df['High']
ac
bd=df['Months']
ef=df['Low']
gh=df['Avg']

Y=range(12)


#The best time to visit Agra is from August to November as the climate at this time is quite pleasant for travelling as average temperature lies between 20 to 29 degree celcius .May month
#is the hottest with 46 degree celcius .On the other hand December and January seems to be the coldest month with as low as 5 degree celcius.


# # The best time to visit Agra is from August to November as the climate at this time is quite pleasant for travelling as average temperature lies between 20 to 29 degree celcius .May month is the hottest with 46 degree celcius .On the other hand December and January seems to be the coldest month with as low as 5 degree celcius.
# 

# In[ ]:



