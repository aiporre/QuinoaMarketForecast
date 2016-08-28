# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 22:15:24 2016

Building a dataset with python

This example uses the datasets provided by
quandl. We use the Quinoa production and 
we build the datasets comparing prices for 
the four producing contries.

@author: aiporre
"""
import quandl 
import pandas as pd
import pickle as pk

def get_producers_list():
    # reads all tables in web page. Result is a list of datasets
    quinoaProducers = pd.read_html('https://en.wikipedia.org/wiki/Quinoa')
    Countries = []
    for q in quinoaProducers[3][0]:
        Countries.append("UFAO/CR_QNOA_" + str(q)[0:3].upper())
    return Countries[1:4]


def get_from_quandl():
    # qp is dataframe from data from a web page
    countries = get_producers_list()

    # put your own apikey from quandl
    api_key = open('data/myApiKey.txt','r').read()
    quinoaProducers = {}

    for country in countries:
        print country
        df = quandl.get(country,authtoken=api_key)
        quinoaProducers[country] = df
    # method 1 python pockiing
    pickle_out = open('data/quinoa_producers1.pickle', 'wb')
    pk.dump(quinoaProducers, pickle_out)
    pickle_out.close()

    #method2 pandas pickling
    # pd.DataFrame(quinoaProducers).to_pickle('data/quinoa_producers2.pickle')

    return quinoaProducers


try:
    # Method 1: python pickling
    pickle_in  = open('data/quinoa_producers1.pickle','rb')
    qp_collection1 = pk.load(pickle_in)
    # Method 2: pandas pickling
    # qp_collection2 = pd.read_pickle('data/quinoa_producers2.pickle')
except:
    qp_collection1 = get_from_quandl()
    # qp_collection2 = qp_collection1

print 'Python pickling collection'
for producer in qp_collection1:
    print producer
    print qp_collection1[producer].head()
# print " Pandas pickling collection"
# print qp_collection2

