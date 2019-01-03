
# coding: utf-8

# In[12]:


import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.style as style
print(plt.style.available)
from IPython.display import display, HTML
df=pd.read_csv('market_agra.csv')


def market(cus_name,city):
    
    plt.close('all')
    if cus_name=='Clothing':
    
        a=df.loc[df['Clothing'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['Clothing'] == True,['Market Name']]
        d=b['Market Name']
        e=df.loc[df['Clothing'] == True,['Market Name','Rating','Address','Famous_for']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')

        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray')
        plt.xlabel('Market Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Clothing')
        plt.show()
        display(e)
    elif cus_name=='Handicraft':
        
        a=df.loc[df['Handicraft'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['Handicraft'] == True,['Market Name']]
        d=b['Market Name']
        e=df.loc[df['Handicraft'] == True,['Market Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray',fontsize=17)
        plt.xlabel('Market Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Handicraft')
        plt.show()
        display(e)
    elif cus_name=='Showpieces':
    
        a=df.loc[df['Showpieces'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['Showpieces'] == True,['Market Name']]
        d=b['Market Name']
        e=df.loc[df['Showpieces'] == True,['Market Name','Rating','Address','Famous_for']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')

        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray')
        plt.xlabel('Market Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Showpieces')
        plt.show()
        display(e)
    elif cus_name=='Agra Special':
    
        a=df.loc[df['Agra Special'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['Agra Special'] == True,['Market Name']]
        d=b['Market Name']
        e=df.loc[df['Agra Special'] == True,['Market Name','Rating','Address','Famous_for']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')

        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray')
        plt.xlabel('Market Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Agra Special')
        plt.show()
        display(e)
    elif cus_name=='Household':
    
        a=df.loc[df['Household'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['Household'] == True,['Market Name']]
        d=b['Market Name']
        e=df.loc[df['Household'] == True,['Market Name','Rating','Address','Famous_for']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')

        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray')
        plt.xlabel('Market Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Household Shops')
        plt.show()
        display(e)
    
test=market('Handicraft',"Bhubaneswar")


# In[13]:

test=market('Household',"Bhubaneswar")


# In[14]:

test=market('Agra Special',"Bhubaneswar")


# In[15]:

test=market('Clothing',"Bhubaneswar")


# In[16]:

test=market('Showpieces',"Bhubaneswar")


# In[ ]:



