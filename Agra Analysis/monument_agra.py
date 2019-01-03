
# coding: utf-8

# In[5]:

#This function takes input whAT type of tourist place travellers likes
import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.style as style
plt.style.available
from IPython.display import display, HTML
import matplotlib.image as mpimg
df2=pd.read_csv('agra_monument.csv')
cus=df2['Type']
df2['photography']=[True if 'Photography' in i else False for i in cus]
df2['worship'] = [True if 'Worship' in i else False for i in cus]
df2['historical'] = [True if 'Historical' in i else False for i in cus]


def monument(monu,city):
    plt.close('all')
    
    if monu=='Photography':
        a=df2.loc[df2['photography'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df2.loc[df2['photography'] == True,['Monument Name']]
        d=b['Monument Name']
        e=df2.loc[df2['photography'] == True,['Monument Name','Rating','Locality','Type']].reset_index(drop=True)
        plt.figure(figsize=(20,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        
        plt.plot(f,u,color='brown',marker='o',linewidth=2,linestyle=':')
    
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,fontsize=13,color='navy')
      
        plt.xlabel('Monument',fontsize=12,color='black')
        plt.ylabel('RATING',fontsize=12,color='black')
        plt.title('Photography',fontsize=15,color='navy')
        plt.show()
        display(e)
    elif monu=='Worship':
        a=df2.loc[df2['worship'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df2.loc[df2['worship'] == True,['Monument Name']]
        d=b['Monument Name']
        e=df2.loc[df2['worship'] == True,['Monument Name','Rating','Locality','Type']].reset_index(drop=True)        
        plt.figure(figsize=(12,6))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,u,color='brown',marker='o',linewidth=2,linestyle=':')
    
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,fontsize=13,color='navy')
      
        plt.xlabel('Monument Name',fontsize=12,color='black')
        plt.ylabel('RATING',fontsize=12,color='black')
        plt.title('Temple',fontsize=15,color='navy')
        plt.show()
        display(e)
    elif monu=='Historical':
        a=df2.loc[df2['historical'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df2.loc[df2['historical'] == True,['Monument Name']]
        d=b['Monument Name']
        e=df2.loc[df2['historical'] == True,['Monument Name','Rating','Locality','Type']].reset_index(drop=True)        
        plt.figure(figsize=(12,6))
        ax=plt.subplot()
        plt.plot(f,u,color='brown',marker='o',linewidth=2,linestyle=':')
    
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,fontsize=13,color='navy')
      
        plt.xlabel('Monument Name',fontsize=12,color='black')
        plt.ylabel('RATING',fontsize=12,color='black')
        plt.title('Historical Place',fontsize=15,color='navy')
        plt.show()
        display(e)
   
  
test=monument('Historical','Bhubaneswar')   



# In[ ]:



