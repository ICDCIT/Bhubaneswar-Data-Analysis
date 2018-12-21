
# coding: utf-8

# In[38]:

#This function takes input whAT type of tourist place travellers likes
import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.style as style
plt.style.available
from IPython.display import display, HTML
import matplotlib.image as mpimg
df2=pd.read_csv('monu.csv')

def monument(monu,city):
    plt.close('all')
    
    if monu=='Temple':
        a=df2.loc[df2['Temple'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df2.loc[df2['Temple'] == True,['Monument Name']]
        d=b['Monument Name']
        e=df2.loc[df2['Temple'] == True,['Monument Name','Rating','Locality']].reset_index(drop=True)
        plt.figure(figsize=(15,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        
        plt.plot(f,u,color='navy',marker='o',linewidth=2,linestyle=':')
    
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,fontsize=13,color='gray')
      
        plt.xlabel('Market Name',fontsize=12,color='navy')
        plt.ylabel('RATING',fontsize=12,color='navy')
        plt.title('Temple',fontsize=15,color='navy')
        plt.show()
        plt.savefig('temples1.png')
        display(e)
    elif monu=='Photography':
        a=df2.loc[df2['Photography'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df2.loc[df2['Photography'] == True,['Monument Name']]
        d=b['Monument Name']
        e=df2.loc[df2['Photography'] == True,['Monument Name','Rating','Locality','Type']].reset_index(drop=True)        
        plt.figure(figsize=(12,6))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,u,marker='o',linewidth=2.1,color='green',linestyle=':')
    
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,fontsize=13,color='gray')
      
        plt.xlabel('Market Name',fontsize=12,color='navy')
        plt.ylabel('RATING',fontsize=12,color='navy')
        plt.title('Malls',fontsize=15,color='navy')
        plt.show()
        plt.savefig('photo.png')
        display(e)
    elif monu=='Parks and Nature':
        a=df2.loc[df2['Parks and Nature'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df2.loc[df2['Parks and Nature'] == True,['Monument Name']]
        d=b['Monument Name']
        e=df2.loc[df2['Parks and Nature'] == True,['Monument Name','Rating','Locality','Type']].reset_index(drop=True)        
        plt.figure(figsize=(12,6))
        ax=plt.subplot()
        plt.plot(f,u,marker='o',linewidth=2.1,color='green',linestyle=':')
    
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,fontsize=13,color='gray')
      
        plt.xlabel('Tourist Place',fontsize=12,color='navy')
        plt.ylabel('RATING',fontsize=12,color='navy')
        plt.title('Park and Nature',fontsize=15,color='navy')
        plt.show()
        plt.savefig('parks.png')
        display(e)
    elif monu=='Museum and Imp. Buildings':
        a=df2.loc[df2['Museum and Imp. Buildings'] == True,['Rating']]
        u=a.Rating
        f=range(len(a))
        b=df2.loc[df2['Museum and Imp. Buildings'] == True,['Monument Name']]
        d=b['Monument Name']
        e=df2.loc[df2['Museum and Imp. Buildings'] == True,['Monument Name','Rating','Locality','Type']].reset_index(drop=True)        
        plt.figure(figsize=(12,6))
        ax=plt.subplot()
        plt.plot(f,u,color='brown',linewidth=2,linestyle=':',marker='o')
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,fontsize=13,color='gray')
        plt.xlabel('Tourist Place',fontsize=12,color='navy')
        plt.ylabel('RATING',fontsize=12,color='navy')
        plt.title('Museum and Imp. building',fontsize=15,color='navy')
        plt.show()
        plt.savefig('museum.png')
        display(e)
   
  
test=monument('Temple','Bhubaneswar')   



# ### In the city of temples you would find hundreds of temple and some of the most visited and loved temples are as follows. Among them Siddeshwar and Makandeswar temple are the most loved temples of the city while Lingraj is also famous for Lord Shiva and see thousands of people travelling to worship Shiva.

# In[39]:

test=monument('Photography','Bhubaneswar')


# ### Photographers travelling to this city generally come here to take nature clicks .Sun temple is the most beauiful place for photography as rated by people following Nandankanan and chilika that gives a natural ambience for a perfect click. 

# In[40]:

test=monument('Parks and Nature','Bhubaneswar')


# ### For nature lovers Nandankanan Zoological Park is the best place to visit as it gives many option like zoo,zoological park and even boating.While Trekking lovers can visit Dhaula Giri Hills .In natural tourist place Chilika lake has also benn voed for its beauty and lake view.

# In[41]:

test=monument('Museum and Imp. Buildings','Bhubaneswar')


# ### If you are too curious to know about tribes and their culture then bbsr has one of the best museums of tribal arts and artifacts wih highest rating in nayapalli while Dhauli Shanti Stupa and Regional Science Centre stands second on tourist list.
# 
