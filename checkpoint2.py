# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 01:27:44 2020

@author: ASUS
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

df=pd.read_csv("train_and_test2.csv")
print(df)




for i in range(1,19):
    
        df.drop('zero.%d'%i,axis=1 ,inplace=True)
df.drop('zero',axis=1 ,inplace=True)        
print(df.columns)

df.dropna(axis=0,how='any',inplace=True)
print(df.isnull().sum().sum())


print(df.head(10))

sns.lmplot("Age","Sex",data=df)

sns.lmplot("Fare","Age",data=df)



def plot_correlation_map( df ):

    corr = df.corr()

    s , ax = plt.subplots( figsize =( 12 , 10 ) )

    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )

    s = sns.heatmap(

        corr, 

        cmap = cmap,

        square=True, 
 
        cbar_kws={ 'shrink' : .9 }, 

        ax=ax, 

        annot = True, 

        annot_kws = { 'fontsize' : 12 }

        )
plot_correlation_map( df )

"""
this function gives the corrolation between every column in the dataset and display it 
in map with a various colors according to the resulted value 
"""

print(pd.DataFrame(dict(list(df["2urvived"].groupby(df["Pclass"])))).mean())



