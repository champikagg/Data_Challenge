import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import pylab
import matplotlib
data = pd.read_csv('new_data.csv')
X=data.Days
Y=data.Items
numBins=3

xmin = X.min()
xmax = X.max()
fig = pylab.figure()
fig.show()
pylab.title('No of Items vs Date')
pylab.xlabel('Date')
pylab.ylabel('Items')
ax = fig.add_subplot(111)	
bins = np.linspace(xmin,xmax,numBins+1)
XX = np.array([np.mean((bins[binInd], bins[binInd+1])) for binInd in range(numBins)])
YY = np.array([np.mean(Y[(X > bins[binInd]) & (X <= bins[binInd+1])]) for binInd in range(numBins)])
lineHandles = ax.scatter(XX,YY)
plt.xticks(np.arange(min(X), max(X)+1, 33.0))

#print lineHandles[0]
print "______________________"
print XX
print "______________________"
print YY
print "______________________"

#print matplotlib.is_interactive()
#print matplotlib.matplotlib_fname()
pylab.pause(2**31-1)


	

