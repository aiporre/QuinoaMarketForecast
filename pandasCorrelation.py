import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

qp = pd.read_pickle('data/quinoa_producers2.pickle')
qp.columns = ['SEED_PER','HARVEST_PER','YIELD_PER','PRODUCTION_PER',
              'SEED_BOL', 'HARVEST_BOL', 'YIELD_BOL', 'PRODUCTION_BOL',
              'SEED_ECU', 'HARVEST_ECU', 'YIELD_ECU', 'PRODUCTION_ECU']

# # Operation with entire columns
# print '='*20 + "Operations in columns" + '='*20
# qp['LABOR_PRODUCTIVITY_ECU'] = qp['PRODUCTION_ECU']/365
# print qp[['PRODUCTION_ECU','LABOR_PRODUCTIVITY_ECU']].head()

print '='*20 + " Ploting data as whole " + '='*20
qp.plot()
plt.legend().remove()
plt.show()

print '='*20 + " Correlation matrix " + '='*20

qp_correlation = qp.corr()
print qp_correlation
print 'Presenting description ... '
print qp_correlation.describe()
