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

data1 = randn(100)
data2 = randn(100)

sns.boxplot([data1,data2])
plt.show()

sns.boxplot([data1,data2],whis=np.inf)
plt.show()


#Normal Dist
data1 = stats.norm(0,5).rvs(100)

#two gamma dist concatenated together
data2= np.concatenate([stats.gamma(5).rvs(50)-1,-1*stats.gamma()])

