import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df_adv = pd.read_csv('new_data.csv')
X = df_adv[['Days', 'Date']]
y = df_adv['Items']
df_adv.head()

## fit a OLS model with intercept on Days and Date
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

est.summary()
# formula: response ~ predictor + predictor
est = smf.ols(formula='Items ~ Days + Date', data=df_adv).fit()