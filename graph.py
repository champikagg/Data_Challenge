# The commands used here is run in ipython command prompt

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import pylab
import matplotlib

df = pd.read_csv("data.csv", names=["Date", "Days", "Items"])
np.mean(df['Days'])
np.median(df['Days'])
np.min(df['Days'])
np.max(df['Days'])
np.cumsum(df['Days'])
df1 = pd.read_csv("groupbydays.csv")
plt.scatter(df1['Days'], df1['Items'])
plt.xlabel('No of Items')
plt.ylabel('No of Days')
plt.title('Items bought vs Days') 

# converting string date to date format
data1 = pd.read_csv('data.csv',	names=["Date", "Days", "Items"],parse_dates={'Timestamp': ['Date']},index_col='Timestamp')
data = pd.read_csv('groupbydate.csv',parse_dates={'Timestamp': ['Date']})
	
# histogram for days
data1.hist('Days',bins=100)

# histogram for items
data1.hist('Items',bins=29)

#date vs items
data.ix['2010-10-25':'2011-02-02','Items'].plot()
plt.ylabel('No of Items')
plt.title('Avg no of Items bought vs Date')
# to make the y axis a log
plt.yscale('log')


# to find correlation between two variables
from scipy.stats import pearsonr
df3 = pd.read_csv("groupbydate.csv")
myitem3=df3.Items
mydays3=df3.Days
np.cov(mydays3,myitem3)
np.corrcoef(mydate,myitem)
