from mpl_toolkits.mplot3d import Axes3D

X = df_adv[['Date', 'Days']]
y = df_adv['Items']

## fit a OLS model with intercept on Date and Days
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

xx1, xx2 = np.meshgrid(np.linspace(X.Date.min(), X.Date.max(), 10), 
                       np.linspace(X.Days.min(), X.Days.max(), 10))

Z = est.params[0] + est.params[1] * xx1 + est.params[2] * xx2

# create matplotlib 3d axes
fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig, azim=-115, elev=15)

# plot hyperplane
surf = ax.plot_surface(xx1, xx2, Z, cmap=plt.cm.RdBu_r, alpha=0.6, linewidth=0)

# plot data points - points over the HP are white, points below are black
resid = y - est.predict(X)
ax.scatter(X[resid >= 0].Date, X[resid >= 0].Date, y[resid >= 0], color='black', alpha=1.0, facecolor='white')
ax.scatter(X[resid < 0].Date, X[resid < 0].Date, y[resid < 0], color='black', alpha=1.0)

# set axis labels
ax.set_xlabel('Date')
ax.set_ylabel('Days')
ax.set_zlabel('Items')