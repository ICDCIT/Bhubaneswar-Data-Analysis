
# coding: utf-8

# In[5]:

from matplotlib import pyplot as plt
from IPython.display import display, HTML

import matplotlib.image as mpimg
plt.figure(figsize=(18,10))
img = mpimg.imread('cost_2.png')
plt.imshow(img)
plt.show()


# In[3]:

#this function is used to show analyis based on cuisines selected  by the user. This function takes cuisine name as input
#and show table and plot graph on the basis of cuisine selected .

import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display, HTML

import matplotlib.image as mpimg

df=pd.read_csv('food_agra_cuisine.csv')

cus=df['Cuisines']
df['chinese']=[True if 'Chinese' in i else False for i in cus]
df['cafe'] = [True if 'Cafe' in i else False for i in cus]
df['north_indian'] = [True if 'North Indian' in i else False for i in cus]
df['mughlai'] = [True if 'Mughlai' in i else False for i in cus]
df['mexican'] = [True if 'Mexican' in i else False for i in cus]
df['continental'] = [True if 'Continental' in i else False for i in cus]
df['italian'] = [True if 'Italian' in i else False for i in cus]
df['rajasthani'] = [True if 'Rajasthani' in i else False for i in cus]

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
        img = mpimg.imread('ch_agra.png')
        plt.imshow(img)
        plt.show()
        display(e)
    elif cus_name=='Cafe':
        
        a=df.loc[df['cafe'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['cafe'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['cafe'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        img = mpimg.imread('cafe_agra.png')
        plt.imshow(img)
        plt.show()
        display(e)
    elif cus_name=='North Indian':
        
        a=df.loc[df['north_indian'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['north_indian'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['north_indian'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        img = mpimg.imread('ni_.png')
        plt.imshow(img)
        plt.show()
        display(e)
    elif cus_name=='Mughlai':
        
        a=df.loc[df['mughlai'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['mughlai'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['mughlai'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        img = mpimg.imread('mug_agra.png')
        plt.imshow(img)
        plt.show()
        display(e)
    elif cus_name=='Continental':
        
        a=df.loc[df['continental'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['continental'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['continental'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        img = mpimg.imread('conti_agra.png')
        plt.imshow(img)
        plt.show()
        display(e)
    elif cus_name=='Italian':
        
        a=df.loc[df['italian'] == True,['Rating']]
        j=a.Rating
        f=range(len(a))
        b=df.loc[df['italian'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        e=df.loc[df['italian'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        img = mpimg.imread('ita_agra.png')
        plt.imshow(img)
        plt.show()
        display(e)
    elif cus_name=='Rajasthani':
        
        a=df.loc[df['rajasthani'] == True,['Rating']]
        j=a.Rating
        b=df.loc[df['rajasthani'] == True,['Restaurant Name']]
        d=b['Restaurant Name']
        f=range(len(d))
        e=df.loc[df['rajasthani'] == True,['Restaurant Name','Rating','Address']].reset_index(drop=True)
        plt.figure(figsize=(18,10))
        img = mpimg.imread('rajasthani_agra.png')
        plt.imshow(img)
        plt.show()
        display(e)
    
test=cusine('',"Agra")


# In[ ]:




# In[ ]:



