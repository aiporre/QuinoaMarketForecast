import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')



def get_gold_price():
    api_key = open('data/myApiKey.txt', 'r').read()
    gold = quandl.get('BUNDESBANK/BBK01_WT5511', authtoken=api_key)
    pd.DataFrame(gold).to_pickle('data/gold.pickle')


try:
    gold = pd.read_pickle('data/gold.pickle')
except:
    gold = get_gold_price()
gold.columns = ['price']
print "Daily gold price "
print gold.head()

print "resampled to annually frequency"
gold_resampled = gold.resample('A')
print gold_resampled.head()

print "Ploting"
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
gold.plot(ax = ax1)
gold_resampled.plot(color = 'k', ax = ax1)
plt.legend().remove()
plt.show()

