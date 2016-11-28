import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
df_wine = pd.read_csv('whitewines.csv',sep=',')


#df_5 = df_wine.head()
#print df_5.describe()
#print df_5.columns.values
wino = df_wine.groupby('quality')
print wino.describe()
def max_to_min(arr):
    return arr.max()-arr.min()

#print df_wine['fixed']
#wino = df_wine.groupby(df_wine['quality'])
#wino.describe()

print wino.agg(max_to_min)

print wino.agg('mean')

df_wine['qual/alc ratio'] = df_wine['quality']/df_wine['alcohol']

print df_wine.head()

print df_wine.pivot_table(index=['quality'])

df_wine.plot(kind='scatter',x='quality',y='alcohol')
plt.show()