import pandas as pd

import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate' : [2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
# contatenation.
concat = pd.concat([df1,df2])
print "Concatenation df1 and df2"
print(concat)
# Notice that there are some holes NaN where data is
# has the same index. It just concatenates and don't
# mix the information, that is why you may find some
# index repetitions and so on.
concat = pd.concat([df1,df2,df3])
print "Concatenation df1 df2 df3"
print(concat)

# Appending
# Append on the other hand my help to manage the problem
# mentioned before since it is using the indices and not
# just piling on dataframes and it mixes its indexed
df4 = df1.append(df2)
print "Appended df2 appended to df1"
print(df4)
# Nevertheless there are some problems when there exists
# information not in common between data frames
df4 = df1.append(df3)
print "appended df3 with missing values or columnes to df1"
print(df4)

# New data
# df are not made to be updated and what is more pandas is not
# made append new information to data frames which means that
# pandas may perform poorly if you want to update delete and add
# new data into your data frame. Nonetheless, if you want to do
# it, yes pandas allows it but un-efficiently add more data.


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
print "df1 and df2 merged on index HP1"
print pd.merge(df1,df2,on = 'HPI')

# to fix you need to make it over a list(dark for me)
print "df1 and df2 merged over a list of indexes HP1 an Int_rate"
print pd.merge(df1,df2, on = ['HPI','Int_rate'])
print "df1 and df2 merged over a list of indexes HP1 an Int_rate"
print pd.merge(df1,df2, on = ['HPI','Int_rate',"US_GDP_Thousands"])

# Joining

# First with reassign the index so the for dataframes df1 and df3

df1.set_index('HPI', inplace = True)
df3.set_index('HPI', inplace = True)
joined  = df1.join(df3)

print "Joined df1 and df3 with new index assignation"
print joined
# we must notice that we have some data replication
# because when the joining is performed then if the index is the
# same but the data is differnet it will consider that as new information
# Lets explore if index are complete different

df1_1 = pd.DataFrame({'Year': [2001, 2002, 2003, 2004],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]})

df3_1 = pd.DataFrame({'Year': [2005, 2006, 2007, 2008],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53]})
df1_1.set_index('Year', inplace=True)
df3_1.set_index('Year', inplace=True)
print "Join with different indexes"
print df1_1.join(df3_1)

# We see that if the index is not in the dataframe the it just doesn't joins the new information
# Let explore that by putting just one different key in each side
df1_2 = pd.DataFrame({'Year': [2001, 2002, 2003, 2004],
                      'Int_rate': [2, 3, 2, 2],
                      'US_GDP_Thousands': [50, 55, 65, 55]})

df3_2 = pd.DataFrame({'Year': [2001, 2002, 2003, 2005],
                      'Unemployment': [7, 8, 9, 6],
                      'Low_tier_HPI': [50, 52, 50, 53]})
df1_2.set_index('Year', inplace=True)
df3_2.set_index('Year', inplace=True)
print "Join with one different index in each side"
print df1_2.join(df3_2)

# We can solve that by merging and joinig
df1_3 = pd.DataFrame({'Year': [2001, 2002, 2003, 2004],
                      'Int_rate': [2, 3, 2, 2],
                      'US_GDP_Thousands': [50, 55, 65, 55]})

df3_3 = pd.DataFrame({'Year': [2001, 2002, 2003, 2005],
                      'Unemployment': [7, 8, 9, 6],
                      'Low_tier_HPI': [50, 52, 50, 53]})
merged_3 = pd.merge(df1_3, df3_3, on='Year')
merged_3.set_index("Year", inplace=True)
print "Merged types: inner(deafault)"
print merged_3
merged_3 = pd.merge(df1_3, df3_3, on='Year', how='outer')
merged_3.set_index("Year", inplace=True)
print "Merged types: inner(outer)"
print merged_3

merged_3 = pd.merge(df1_3, df3_3, on='Year', how='left')
merged_3.set_index("Year", inplace=True)
print "Merged types: inner(left)"
print merged_3


# main focus of merge is mix in column
# join index are important, and respect it existente
# DF similar merge with column and dnt care about the indexes
# DF may no use contatenation





