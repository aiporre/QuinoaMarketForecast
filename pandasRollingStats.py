
import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')



def get_zinc_price():
    api_key = open('data/myApiKey.txt', 'r').read()
    gold = quandl.get('ODA/PZINC_USD', authtoken=api_key)
    pd.DataFrame(gold).to_pickle('data/zinc.pickle')

def get_wheat_price():
    api_key = open('data/myApiKey.txt', 'r').read()
    gold = quandl.get('ODA/PWHEAMT_USD', authtoken=api_key)
    pd.DataFrame(gold).to_pickle('data/wheat.pickle')


fig = plt.figure()
ax1 = plt.subplot2grid((4,1),(0,0))
ax2 = plt.subplot2grid((4,1),(1,0))
ax3 = plt.subplot2grid((4,1),(2,0))
ax4 = plt.subplot2grid((4,1),(3,0))
# read prices of zinc
try:
    zinc = pd.read_pickle('data/zinc.pickle')
except:
    zinc = get_zinc_price()
# read prices of wheat
try:
    wheat = pd.read_pickle('data/wheat.pickle')
except:
    wheat = get_wheat_price()
# calculatin rollings
zinc.columns = ['price_z']
wheat.columns = ['price_w']
zw = zinc.join(wheat)
zinc['priceRA'] = pd.rolling_mean(zinc['price_z'],12)
zinc['priceRS'] = pd.rolling_std(zinc['price_z'],12)
print zw.head(10)
zinc_wheat_corr = pd.rolling_corr(zw['price_z'],zw['price_w'],12)
print zinc.head(15)
print zinc_wheat_corr.head(15)
# zinc.dropna(inplace = True) # posible to use dorpna
zinc[['price_z','priceRA']].plot(ax = ax1)
zinc['priceRS'].plot(ax = ax2)
zw.plot(ax = ax3)
zinc_wheat_corr.plot(ax = ax4)
plt.show()

# standrd deviatio help to filter date that doesnlt fit
# an to undersatd the volatitty of the data.


