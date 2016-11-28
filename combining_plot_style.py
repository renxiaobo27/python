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

dataset = randn(100)

sns.distplot(dataset,bins=25,rug=True,hist=False)
plt.show()

sns.distplot(dataset,bins=25,kde_kws={'color':'indianred','label':'KDE PLOT'},
             hist_kws={'color':'blue','label':'HIST'})

plt.show()

ser1 = Series(dataset,name='My_data')
print ser1
sns.plot(ser1,bins=25)