
import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')



def get_gold_price():
    api_key = open('data/myApiKey.txt', 'r').read()
    gold = quandl.get('ODA/PZINC_USD', authtoken=api_key)
    pd.DataFrame(gold).to_pickle('data/zinc.pickle')


try:
    zinc = pd.read_pickle('data/zinc.pickle')
except:
    zinc = get_gold_price()
zinc.columns = ['price']
print "Daily zinc price "
print zinc.head()

print "resampled to weekly frequency"
zinc_resampled = zinc.resample('A')
print zinc_resampled.head()


print " dealing with NaN data"

zinc.columns = ['daily']

# gold['price_week'] = gold_resampled
df = zinc.join(zinc_resampled, how ='outer')
df.columns = ['month', 'quater']
print df.head(10)
print "NaN cleared"
# df.dropna( how = 'all' , inplace= True)
# df.fillna(method='ffill', inplace=True)
df.fillna(method='bfill', inplace=True)
print df.head(10)

# # leave like that graph
# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))
# df.plot(ax = ax1)
# zinc_resampled.plot(color = 'k', ax = ax1)
# plt.legend().remove()
# plt.title('With empty values')
# plt.show()

# deleted rows
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
df.plot(ax = ax1)

df['month'].plot(ax=ax1)
df['quater'].plot(ax= ax1)
plt.title('managed nan')
plt.show()


