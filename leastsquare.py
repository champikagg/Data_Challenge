# Linear regression is one of the simplest and most commonly used modeling techniques. 
# It makes very strong assumptions about the relationship between the predictor variables (the X) and the response (the Y). 
# It assumes that this relationship takes the form: y=β0+β1*x
# Ordinary Least Squares is the simplest and most common estimator in which the two βs are chosen to minimize the square of 
# the distance between the predicted values and the actual values.

# load numpy and pandas for data manipulation
import numpy as np
import pandas as pd

import statsmodels.api as sm

df = pd.read_csv("data.csv", names=["Date", "Days", "Items"])
df.head()

y = df3.Items  # response
X = df3.Days  # predictor
X = sm.add_constant(X)  # Adds a constant term to the predictor
X.head()

est = sm.OLS(y, X)
est = est.fit()
est.summary()
est.params


# We pick 100 hundred points equally spaced from the min to the max
X_prime = np.linspace(X.Days.min(), X.Days.max(), 100)[:, np.newaxis]
X_prime = sm.add_constant(X_prime)  
# Now we calculate the predicted values
y_hat = est.predict(X_prime)

plt.scatter(X.Days, y, alpha=0.3)  # Plot the raw data
plt.xlabel("No of Days")
plt.ylabel("No of Items bought")
plt.plot(X_prime[:, 1], y_hat, 'r', alpha=0.9)  # Add the regression line, colored in red



