import pandas as pd
import numpy as np
import csv
import datetime
from datetime import date, datetime
import matplotlib.pyplot as plt


df = pd.read_csv("data.csv", names=["Date", "Days", "Items"])
print df.describe()
names=["Days","Items"]
file = open("descriptive.txt", "wb")
writer = csv.writer(file)
file.write("mean \t median \t minimum \t maximum \t standard deviation \t variance\n")
for name in names:
	
	data_mean = np.mean(df[name])#	Mean of values
	data_median = np.median(df[name])	#Arithmetic median of values
	data_min = np.min(df[name])	#Minimum
	data_max = np.max(df[name])#	Maximum
	data_std = np.std(df[name]) #	Unbiased standard deviation
	data_var = np.var(df[name]) #	Unbiased variance
	x=data_mean,data_median,data_min,data_max,data_std,data_var
	my_mean=str(data_mean)
	my_median=str(data_median)
	my_min=str(data_min)
	my_max=str(data_max)
	my_std=str(data_std)
	my_var=str(data_var)
	file.write(name)
	file.write("\n")
	file.write(my_mean)
	file.write("\t")
	file.write(my_median)
	file.write("\t")
	file.write(my_min)
	file.write("\t")
	file.write(my_max)
	file.write("\t")
	file.write(my_std)
	file.write("\t")
	file.write(my_var)
	file.write("\n")

file.close()
file = open('descriptive.txt', 'r')
print file.read()







