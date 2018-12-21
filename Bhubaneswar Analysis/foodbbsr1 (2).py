
# coding: utf-8

# In[2]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('cost for 2.png')
plt.figure(figsize=(20,14))
plt.imshow(img)


plt.show()


# # Unit 4 was found to be the cheapest place to dine in while Patia area is also having many affordable restaurants.The Crown was found to be he most expensive restaurant in Bhubaneswar

# In[47]:

#this function is used to show analyis based on cuisines selected  by the user. This function takes cuisine name as input
#and show table and plot graph on the basis of cuisine selected .

import pandas as pd 
import numpy as np
import matplotlib.style as style
from matplotlib import pyplot as plt
from IPython.display import display, HTML
df=pd.read_csv('food.csv')
b=df.loc[df['Cuisines'] == 'Chinese',['Restaurant Name']]
cus=df['Cuisines']
df['chinese']=[True if 'Chinese' in i else False for i in cus]
df['cafe'] = [True if 'Cafe' in i else False for i in cus]
df['north_indian'] = [True if 'North Indian' in i else False for i in cus]
df['asian'] = [True if 'Asian' in i else False for i in cus]
df['mexican'] = [True if 'Mexican' in i else False for i in cus]
df['continental'] = [True if 'Continental' in i else False for i in cus]
df['italian'] = [True if 'Italian' in i else False for i in cus]
df['fast_food'] = [True if 'Fast Food' in i else False for i in cus]

def cusine(cus_name,city):
    
    cus=df['Cuisines']
    plt.close('all')
    if cus_name=='Chinese':
    
        a=df.loc[df['chinese'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['chinese'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['chinese'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')

        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray')
        plt.xlabel('Restaurant Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Chinese')
        plt.show()
        plt.savefig("chineseq.png")
        display(e)
    elif cus_name=='Cafe':
        
        a=df.loc[df['cafe'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['cafe'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['cafe'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray',fontsize=17)
        plt.xlabel('Restaurant Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Cafe')
        plt.show()
        plt.savefig("cafe.png")
        display(e)
    elif cus_name=='North Indian':
        
        a=df.loc[df['north_indian'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['north_indian'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['north_indian'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray',fontsize=17)
        plt.xlabel('Restaurant Name',color='brown')
        plt.ylabel('RATING',color='brown')

        plt.title('North Indian')
        plt.show()
        plt.savefig("north.png")
        display(e)
    elif cus_name=='Asian':
        
        a=df.loc[df['asian'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['asian'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['asian'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')

        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray',fontsize=17)
        plt.xlabel('Restaurant Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Asian Food')

        plt.show()
        plt.savefig("asian.png")
        display(e)
    elif cus_name=='Mexican':
        plt.close('all')
        a=df.loc[df['mexican'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['mexican'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['mexican'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')

        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray',fontsize=17)
        plt.xlabel('Restaurant Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Mexican food')

        plt.show()
        plt.savefig("mexican.png")
        display(e)
    elif cus_name=='Continental':
        
        a=df.loc[df['continental'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['continental'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['continental'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')

        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray',fontsize=17)
        plt.xlabel('Restaurant Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Continental Food')

        plt.show()
        plt.savefig('conti.png')
        display(e)
    elif cus_name=='Italian':
        
        a=df.loc[df['italian'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['italian'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['italian'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')

        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray',fontsize=17)
        plt.xlabel('Restaurant Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Italian')

        plt.show()
        plt.savefig("italian.png")
        display(e)
    elif cus_name=='Fast Food':
        
        a=df.loc[df['fast_food'] == True,['Rating']]
        j=a.Rating
        b=df.loc[df['fast_food'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        f=range(len(d))
        e=df.loc[df['fast_food'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        ax=plt.subplot()
        plt.style.use('fivethirtyeight')
        plt.plot(f,j,color='brown',marker='o',linestyle='--',linewidth=2)
        ax.set_xticks(f)
        ax.set_xticklabels(d,rotation=30,color='gray',fontsize=17)
        plt.xlabel('Restaurant Name',color='brown')
        plt.ylabel('RATING',color='brown')
        plt.title('Fast food ')
       
        plt.show()
        plt.savefig("fast.png")
        display(e)
    
test=cusine('North Indian',"Bhubaneswar")


# In[ ]:




# In[ ]:




# In[ ]:



