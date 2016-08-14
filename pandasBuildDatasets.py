# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 00:15:24 2016

Building a dataset with python

This example uses the datasets provided by
quandl. We use the Quinoa production and 
we build the datasets comparing prices for 
the four producing contries.

@author: aiporre
"""
import quandl 
import pandas as pd

# read all tables in web page. Result is a list of datasets
quinoaProducers = pd.read_html('https://en.wikipedia.org/wiki/Quinoa')
print quinoaProducers[3]
df = quinoaProducers[3][0]
df.to_csv('quinoaProducers.csv')

# qp is dataframe from data from a web page
qp = pd.read_csv('quinoaProducers.csv')
# print qp
quinoaProcucer = qp.Country

Countries = []
for q in quinoaProcucer:
    Countries.append("UFAO/CR_QNOA_" + str(q)[0:3].upper())
# put your own apikey from quandl
api_key = open('myApiKey.txt','r').read()

print Countries[0]
df1 = quandl.get(Countries[0], authtoken=api_key)

print Countries[1]
df2 = quandl.get(Countries[1], authtoken=api_key)

print Countries[2]
df3 = quandl.get(Countries[2], authtoken=api_key)

print df1.head()
print df2.head()
print df3.head()

df1.to_csv('filePer.csv')
df2.to_csv('fileBol.csv')
df3.to_csv('fileEcu.csv')

qp_per = pd.read_csv('filePer.csv')
qp_bol = pd.read_csv('fileBol.csv')
qp_ecu = pd.read_csv('fileEcu.csv')


print "Dataframe peru: " + str(qp_per.head())
print "Dataframe bolivia: " + str(qp_bol.head())
print "Dataframe ecuador: " + str(qp_ecu.head())

# for i in range(0,3):
#     df  = quandl.get(Countries[i], authtoken = api_key)








