import pandas as pd

import pandas as pd

# df1 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'US_GDP_Thousands':[50, 55, 65, 55]},
#                    index = [2001, 2002, 2003, 2004])
#
# df2 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'US_GDP_Thousands':[50, 55, 65, 55]},
#                    index = [2005, 2006, 2007, 2008])
#
# df3 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'Low_tier_HPI':[50, 52, 50, 53]},
#                    index = [2001, 2002, 2003, 2004])
# # contatenation.
# concat = pd.concat([df1,df2])
# print(concat)
# # Notice that there are some holes NaN where data is
# # has the same index. It just concatenates and don't
# # mix the information, that is why you may find some
# # index repetitions and so on.
# concat = pd.concat([df1,df2,df3])
# print(concat)
#
# # Appending
# # Append on the other hand my help to manage the problem
# # mentioned before since it is using the indices and not
# # just piling on dataframes and it mixes its indexed
# df4 = df1.append(df2)
# print(df4)
# # Nevertheless there are some problems when there exists
# # information not in common between data frames
# df4 = df1.append(df3)
# print(df4)
#
# # New data
# # df are not made to be updated and what is more pandas is not
# # made append new information to data frames which means that
# # pandas may perform poorly if you want to update delete and add
# # new data into your data frame. Nonetheless, if you want to do
# # it you can add more data.


#################### Merging

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
# Repeated data. It is becasuse the index
print pd.merge(df1,df2,on = 'HPI')

# to fix you need to make it over a list(dark for me)
print pd.merge(df1,df2, on = ['HPI','Int_rate'])




