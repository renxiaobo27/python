import numpy as np
import pandas as pd
from pandas import Series,DataFrame


animals = DataFrame(np.arange(16).reshape(4,4),columns=['W','X','Y','Z'],index=['Dog','Cat','Bird','Mouse'])

print animals

animals.ix[1:2,['W','Y']] = np.nan

behavior_map = {'W':'good','X':'bad','Y':'good'}

animals_col = animals.groupby(behavior_map,axis=1)

print animals_col.sum()

behav_series = Series(behavior_map)
print behav_series

print animals.groupby(behav_series,axis=1).count()

#index length
print animals.groupby(len).sum()

keys = ['A','B','A','B']
print animals.groupby([len,keys]).max()

#hirachy
hier_col = pd.MultiIndex.from_arrays([['NY','NY','NY','SF','SF'],[1,2,3,1,2]],names=['City','sub_value'])
df_hr = DataFrame(np.arange(25).reshape(5,5),columns=hier_col)
df_hr = 100*df_hr
print df_hr