# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 18:01:17 2016

@author: aiporre
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

cancer_stats = {'Sizes': [21,35,12,31,51,12],
                'Patients': [1,2,3,4,5,6],
                'Densities':[0.23,1.124,0.031,0.111,0.4111,1.923]}
# setting data frame
                
df =  pd.DataFrame(cancer_stats)

## scratching data
print(df)
print(df.head())
print(df.tail())
print(df.head(2))

### new indexed data
print(df.set_index('Patients')) # return data with a new dataframe

df_indexed = df.set_index('Patients')
print(df_indexed.head())

## auto denominate
df.set_index('Patients',inplace = True)
print(df.head())



## select columns
print(df['Sizes'])
print(df.Sizes) # easy but is needed to avoid the use of spaces in labels
print df[['Sizes','Densities']]

## Dataframe convertions
# to list
print(df.Sizes.tolist)
my_array = np.array(df[['Sizes','Densities']])
print(my_array)

# arrays can be converted to dataframes

df2 = pd.DataFrame(my_array)
print(df2)
