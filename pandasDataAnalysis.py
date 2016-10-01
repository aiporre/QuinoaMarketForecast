import quinoaprods as quinoa
import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

def get_quinoa():
    qp = quinoa.as_dataframe()
    qp.columns = ['seed_per','harvest_per','yield_per','prod_per',
              'seed_bol', 'harvest_bol', 'yield_bol', 'prod_bol',
              'seed_ecu', 'harvest_ecu', 'yield_ecu', 'prod_ecu']
    return qp

def get_gold_price():
    try:
        gold = pd.read_pickle('data/gold.pickle')
    except:
        api_key = open('data/myApiKey.txt', 'r').read()
        gold = quandl.get('BUNDESBANK/BBK01_WT5511', authtoken=api_key)
        pd.DataFrame(gold).to_pickle('data/gold.pickle')
    gold.columns = ['gold_price']

    return gold.resample('A')

'''
Sometimes data came with different values and you need to resample
and eliminate ranges of index or maybe fill them.
'''

quinoa_data = get_quinoa()
gold_price = get_gold_price()

exploring_data = quinoa_data.join(gold_price,how='outer')
exploring_data.dropna(inplace = True)
# print exploring_data.head(10)

'''Once you have join the data is time to analyze correlations and
determine whether or not add more data, or even eliminate, that is data
 analysis, and data scientists ought look for hidden pattens decide and
 make conjectures form this information. In this particular exploration
 we see how gold price affects the agricultural process of quinua annually.'''

print exploring_data.corr()
print exploring_data.corr()['gold_price'].describe()
'''the mean about 0.24 indicates a little correlation we may find other data
to create predictions or calculate growing indicators.'''


