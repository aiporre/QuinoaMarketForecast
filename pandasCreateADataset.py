import quinoaprods as quinoa
import pandas as pd
import quandl
import numpy as np
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

def get_gdp_bol():
    try:
        gdp = pd.read_pickle('data/gdp.pickle')
    except:
        api_key = open('data/myApiKey.txt', 'r').read()
        gdp = quandl.get('WWDI/BOL_NY_GDP_MKTP_KD_ZG', authtoken=api_key)
        pd.DataFrame(gdp).to_pickle('data/gdp.pickle')
    gdp.columns = ['gdp_bol']
    return gdp

def get_cpi_bol():
    try:
        cpi = pd.read_pickle('data/cpi.pickle')
    except:
        api_key = open('data/myApiKey.txt', 'r').read()
        cpi = quandl.get('WWDI/BOL_FP_CPI_TOTL_ZG', authtoken=api_key)
        pd.DataFrame(cpi).to_pickle('data/cpi.pickle')
    cpi.columns = ['cpi_bol']
    return cpi
def get_diesel_bol():
    try:
        diesel = pd.read_pickle('data/diesel.pickle')
    except:
        api_key = open('data/myApiKey.txt', 'r').read()
        diesel = quandl.get('UENG/DL_EXPIMP_BOL', authtoken=api_key)
        pd.DataFrame(diesel).to_pickle('data/diesel.pickle')
    diesel.columns = ['import_diesel','export_diesel']
    return diesel

def transform_date(date):
    try:
        date1 = "{:.0f}".format(date) + '-12-31'
        new_date = pd.to_datetime(date1)
    except:
        new_date = date
    return new_date

def get_quinoa_price():
    try:
        price = pd.read_pickle('data/quinoa_price.pickle')
    except:
        df = pd.read_csv('data/quinoaPriceBol.csv',sep=',')
        df['Date'] = list(map(transform_date, df['Year']))
        price = df[['Date','Value']]
        price.columns = ['date','market_price']
        price.set_index('date', inplace=True)
        pd.DataFrame(price).to_pickle('data/quinoa_price.pickle')
    return price
'''
  We must decide from a wide variety of information that could be
  relevant or not to the machine learning task. However, generally
  we must follow the following steps, first define the question that
  you are aiming to response, that means analyze the situation and
  precisely define what you are intersted  on , for instance
  in the case of Bolivia currently the country is interested on investing
  in quinoa production, besides the market price got low because a over production.
  The production could depend on weather, consumer indexes, gross product, surrounding
  competitors and so forth, who knows. The question that we what to answer here is whether or not
  increment quinoa production for the goodness of the country's economy. For that we would
  like predict if is recommended increment production or not.
'''

quinoa_production = get_quinoa()
gold_price = get_gold_price()
cdp_bol = get_gdp_bol()
cpi_bol= get_cpi_bol()
diesel_data = get_diesel_bol()
quinoa_price =  get_quinoa_price()

exploring_data = quinoa_production.join(
    [gold_price,cdp_bol,cpi_bol,diesel_data,quinoa_price])
'''
    Cleaning data
'''
exploring_data.replace({'export_diesel':{ np.nan : 0}},inplace=True)
exploring_data.replace({'import_diesel':{np.nan : 0}}, inplace=True)
exploring_data.interpolate(limit = 500 ,limit_direction = 'backward',inplace=True)
exploring_data.drop('export_diesel', axis=1, inplace=True)
pd.DataFrame(exploring_data).to_pickle('data/exploration.pickle')
# print exploring_data.head()



'''At this point we want to explore relationship across columns '''

# print exploring_data.corr()
# print exploring_data.corr()['market_price'].describe()

'''Not really the best scene but some of these have a reasonable good cross-variance
 in the cases which that is above 0.4, and we can presume that these variables ravel
 some valuable information for the question that we want to answer. Now we will create the
 labels for our classification. For this purpose, we need to add a metric and predict if
 the situation was good or not for the country's economy. We will use cpi and gdp as metrics
 to predict a good or bad situations. that is:
    ++ gpd  -- cpi  : good
    ++ gpd  -- cpi  : bad
    -- gpd  ++ cpi  : bad
    -- gpd  ++ cpi  : bad
 then we create the column label.
'''
exploring_data['fut_cpi_bol'] = exploring_data['cpi_bol'].shift(-1)
exploring_data['fut_gdp_bol'] = exploring_data['gdp_bol'].shift(-1)
exploring_data.dropna(inplace=True)

def create_labels(future_1,current_1,future_2,current_2):
    inc_1 =  future_1 - current_1 > 0
    inc_2 =  future_2 - current_2 < 0
    label = 0
    if inc_1 & inc_2:
        label = 1
    return label

# new_column = list(map( function_to_map, parameter1, parameter2, ... ))
exploring_data['good_business'] = list(map(create_labels,
                                   exploring_data['fut_gdp_bol'],
                                   exploring_data['gdp_bol'],
                                   exploring_data['fut_cpi_bol'],
                                   exploring_data['cpi_bol']))

print exploring_data.tail()

exploring_data.to_csv('data/quinoaBusiness.csv')
