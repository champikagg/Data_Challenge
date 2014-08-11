import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import pylab
import matplotlib

df = pd.read_csv("data.csv", names=["Date", "Days", "Items"])

print df.isnull()