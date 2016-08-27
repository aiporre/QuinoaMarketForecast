# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 19:40:22 2016

Pandas IO

Basics excersices practicing pandas

Pandas help to manage information in same way no matters its format, that means
that you can use the same commands and literary write the same code for 
datasets completly different. You may use csv, xml or many other formats 
as outputs or inputs, which means that you can have for example a csv input
and a xml output or the same way around. 

@author: aiporre
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df =  pd.read_csv('data/BCB-3105.csv')
print df.head()

df.set_index('Date', inplace = True)
df.to_csv('data/newcsv2.csv')
df = pd.read_csv('data/newcsv2.csv')
print df.head()

#you can specify the index when you read it
df = pd.read_csv('data/newcsv2.csv', index_col=0)
print df.head()

# you can rename colums every single column
df.columns = ['BoBraExport']
print df.head()
df.to_csv('data/newcsv3.csv')# save to a csv fie

# may you don want the name in the file so 
# pandas can manage this

df.to_csv('data/newcsv4.csv',header = False)# save to a csv fie

# we can do all the above in one command line
df = pd.read_csv('data/newcsv4.csv',names = ['Date','Bolivia exports to Brazil'], index_col=0)# save to a csv fie
print df.head() # doesn't affect the data

#######
# converting to other formats
df.to_html('data/bobraexport.html')

df = pd.read_csv('data/newcsv4.csv', names=['Date','Exports'],index_col=0)
print df.head()


###########
# visualization

# one column
ts = df.cumsum()
print "Plotting " + str(ts)
df.plot()
plt.title("Exports from Bolivia to Brazil")
plt.xlabel("date (End of month)")
plt.ylabel("Amount of exports")
plt.show()

# One column
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()


# more than one column
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
print df.head()
df = df.cumsum()
plt.figure(); df.hist()
plt.show()




