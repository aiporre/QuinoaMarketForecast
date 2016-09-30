import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import quinoaprods as qdata

# fig =  plt.figure()
# ax1 = plt.subplot2grid((1,1),(0,0))

# we can operate over datasets and recasted them
qp = qdata.as_dataframe()
qp['PROD_PER'] = 2 * qp['Production Quantity - tonnes_PER']
print qp['PROD_PER'].head(3)

# we can plot al the data from this point
qp.plot()
plt.legend().remove()
plt.title("normal")
plt.show()

# we can apply a percent change
qp_pchanged = qp.pct_change()
qp_pchanged.plot()
plt.legend().remove()
plt.title("percent change")
plt.show()

# que can obtain correlation tables

qp_correlation = qp.corr()
print "correlation"
print qp_correlation.describe()