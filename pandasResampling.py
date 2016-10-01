'''
check

Resample rule:
xL for milliseconds
xMin for minutes
xD for Days

Alias	Description
B	business day frequency
C	custom business day frequency (experimental)
D	calendar day frequency
W	weekly frequency
M	month end frequency
BM	business month end frequency
CBM	custom business month end frequency
MS	month start frequency
BMS	business month start frequency
CBMS	custom business month start frequency
Q	quarter end frequency
BQ	business quarter endfrequency
QS	quarter start frequency
BQS	business quarter start frequency
A	year end frequency
BA	business year end frequency
AS	year start frequency
BAS	business year start frequency
BH	business hour frequency
H	hourly frequency
T	minutely frequency
S	secondly frequency
L	milliseonds
U	microseconds
N	nanoseconds

How:
mean, sum, ohlc

'''

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
gold_resampled = gold.resample('W')
print gold_resampled.head()

print "Ploting"
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))


print " dealing with NaN data"

gold.columns = ['daily']

df  =  gold.join(gold_resampled)
print df.head(100)
print "NaN cleared"
print df.dropna(how = 'all', inplace= True)

gold.plot(ax = ax1)
gold_resampled.plot(color = 'k', ax = ax1)
plt.legend().remove()
plt.show()