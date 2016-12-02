import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

#stats
from scipy import  stats

#plot
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print tips.head()

sns.lmplot('total_bill','tip',tips)
plt.show()

sns.lmplot('total_bill','tip',tips,scatter_kws={'marker':'o','color':'red'},
           line_kws={'linewidth':1,'color':'blue'})
plt.show()

sns.lmplot('total_bill', 'tip', tips, order=4,scatter_kws={'marker': 'o', 'color': 'red'},
           line_kws={'linewidth': 1, 'color': 'blue'})
plt.show()


sns.lmplot('total_bill','tip',tips,fit_reg=False)
plt.show()

tips['tip_pect']=100*(tips['tip']/tips['total_bill'])
print tips.head()

sns.lmplot('size','tip_pect',tips)
plt.plot()

#with jetter
sns.lmplot('size','tip_pect',tips,x_jitter=.1)
plt.plot()

# x_estimator : callable that maps vector -> scalar, optional
# Apply this function to each unique value of x and plot the resulting estimate.
# This is useful when x is a discrete variable.
# If x_ci is not None, this estimate will be bootstrapped
# and a confidence interval will be drawn.
sns.lmplot('size','tip_pect',tips,x_estimator=np.mean)
plt.plot()


#hue
sns.lmplot('size','tip_pect',tips,hue='sex',markers=['x','o'])
plt.show()

sns.lmplot('total_bill','tip_pect',tips,hue='day')
plt.show()

#local regression
#loess
sns.lmplot('total_bill','tip_pect',tips,lowess=True,line_kws={'color':'black'})
plt.show()

sns.regplot('total_bill','tip_pect',tips)
plt.show()


#subplot
fig,(axis1,axis2) = plt.subplot(1,2,sharey=True)

sns.regplot('total_bill','tip_pect',tips,ax=axis1)
sns.violinplot(tips['tip_pect'],tips['size'],color='Red_r',ax=axis2)