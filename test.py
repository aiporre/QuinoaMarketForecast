import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('data/100.dat','r') as f:
    next(f)
    df = pd.DataFrame(l.rstrip().split() for l in f)
print df.head()
print '===================================================='
myarray = np.fromfile('data/100.dat',dtype=float)
print np.shape(myarray)
myarray = np.transpose(myarray)
for a  in myarray:
    if a == np.NAN:
        print a

plt.plot(myarray.astype(int)[1:10])
plt.title("signal")
plt.show()