
# coding: utf-8

# In[20]:

#fuction takes the city name as well as  type of market user wants and shows analysis according to it
import pandas as pd 
import numpy as np
import matplotlib.style as style
plt.style.available
from matplotlib import pyplot as plt
from IPython.display import display, HTML


df1=pd.read_csv('marketms1.csv')
plt.close('all')
def market(mar_name,city):
    if mar_name=='Odisha Special':
        a=df1.loc[df1['Odisha Special'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df1.loc[df1['Odisha Special'] == True,['Market_name']]
        d=b['Market_name']
        e=df1.loc[df1['Odisha Special'] == True,['Market_name','Rating','Address','Famous_for']].reset_index(drop=True)
        plt.figure(figsize=(12,6))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,u,marker='o',linewidth=1.1,color='brown')
    
        ax.set_xticks(f)
        e
        ax.set_xticklabels(d,rotation=30,fontsize=15,color='gray')
    
        plt.xlabel('Market Name',fontsize=13,color='navy')
        plt.ylabel('RATING',fontsize=13,color='navy')
        plt.title('Odisha Special Market',fontsize=15,color='blue')
        plt.show()
        display(e)
    elif mar_name=='Mall':
        a=df1.loc[df1['Mall'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df1.loc[df1['Mall'] == True,['Market_name']]
        d=b['Market_name']
        e=df1.loc[df1['Mall'] == True,['Market_name','Rating','Address','Famous_for']].reset_index(drop=True)
        plt.figure(figsize=(12,6))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,u,marker='o',linewidth=1.1,color='brown')
    
        ax.set_xticks(f)
        
        e
        ax.set_xticklabels(d,rotation=30,fontsize=15,color='gray')
      
        plt.xlabel('Market Name',fontsize=13,color='navy')
        plt.ylabel('RATING',fontsize=13,color='navy')
        plt.title('Malls',fontsize=15,color='navy')
        plt.show()
        display(e)
    elif mar_name=='Cinema':
        a=df1.loc[df1['Cinema'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df1.loc[df1['Cinema'] == True,['Market_name']]
        d=b['Market_name']
        e=df1.loc[df1['Cinema'] == True,['Market_name','Rating','Address','Famous_for']].reset_index(drop=True)
        plt.figure(figsize=(12,6))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,u,marker='o',linewidth=1.1,color='brown',linestyle=':')
    
        ax.set_xticks(f)
        
        e
        ax.set_xticklabels(d,rotation=30,fontsize=15,color='gray')
      
        plt.xlabel('Market Name',fontsize=13,color='navy')
        plt.ylabel('RATING',fontsize=13,color='navy')
        plt.title('Cinema',fontsize=15,color='navy')
        plt.show()
        display(e)
    elif mar_name=='Clothing':
        a=df1.loc[df1['Clothing'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df1.loc[df1['Clothing'] == True,['Market_name']]
        d=b['Market_name']
        e=df1.loc[df1['Clothing'] == True,['Market_name','Rating','Address','Famous_for']].reset_index(drop=True)
        plt.figure(figsize=(12,6))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,u,marker='o',linewidth=1.1,color='brown')
    
        ax.set_xticks(f)
        
        e
        ax.set_xticklabels(d,rotation=30,fontsize=15,color='gray')
      
        plt.xlabel('Market Name',fontsize=13,color='navy')
        plt.ylabel('RATING',fontsize=13,color='navy')
        plt.title('Clohing',fontsize=15,color='navy')
        plt.show()
        print('---------------------------------------------------------------------------------------------------------------')
        display(e)
   
  
test=market('Clothing','Bhubaneswar')   



# # If you love handicrafts then bbsr has one of the best Odisha Handicraft market called "Soumya Handicraft" located in Hirapur,Khorda while Utkalika and  Ekmara Hart are also high rated and very famous among tourists and locals. 

# In[16]:


test=market('Mall','Bhubaneswar')


# # If you like to do lots of shopping a malls then bbsr gives a number of options. Most famous is Esplanade mall which is having all the famous brand shops and various things to do their while market building is considered one of the cheapest markets in Bhubaneswar

# In[13]:


test=market('Cinema','Bhubaneswar')


# # If you love to watch movies then Bhubaneswar is having 4 options. Esplanade Mall has been voted for having the best Cinema Hall in whole city.

# In[15]:


test=market('Clothing','Bhubaneswar')


# ###### Finally if you love to do shopping for clothes ,food,etc. then it gives a numerous option .With Esplanade having the highest rating as people voted ,market building is famous for its cheap products.

# In[ ]:



