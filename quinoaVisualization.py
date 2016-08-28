# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 19:15:24 2016

Data analysis on a dataset corresponding to the production of quinoa
world wide.

@author: aiporre
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

qp_per = pd.read_csv('data/filePer.csv', index_col=0)
qp_bol = pd.read_csv('data/fileBol.csv', index_col=0)
qp_ecu = pd.read_csv('data/fileEcu.csv', index_col=0)

## extracting features
bol = np.array(qp_bol[['Production Quantity - tonnes']])
per = np.array(qp_per[['Production Quantity - tonnes']])
ecu = np.array(qp_ecu[['Production Quantity - tonnes']])

print "Bolivia production (first ten years) " + str(np.transpose( bol[0:10,:]))
print "Peru production (first ten years) " + str(np.transpose(per[0:10,:]))
print "Ecuador production (first ten years) " + str(np.transpose(ecu[0:10,:]))

### plotting
qp_bol.plot(subplots = True)
qp_per.plot(subplots = True)
qp_ecu.plot(subplots = True)


plt.figure(4)
plt.title("Quinoa Producers")
plt.xlabel("time [years]")
plt.ylabel("Production Quantity [tonnes]")
bolivia_fig, = plt.plot(bol,'r', label = 'Bo')
peru_fig, = plt.plot(per,'b', label =  'Pe')
ecuador_fig, = plt.plot(ecu,'g', label = 'Ec')
plt.legend([bolivia_fig, peru_fig, ecuador_fig], ['Bolivia','Peru','Ecuador'], bbox_to_anchor=(0.3, 1))
plt.show()

