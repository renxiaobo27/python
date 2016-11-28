import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import pandas.util.testing as tm; tm.N = 3

#Create a unpivoted function

def unpivot(frame):
    N,K = frame.shape

    data = {'value':frame.values.ravel('F'),
            'variable':np.asarray(frame.columns).repeat(N),
            'date':np.tile(np.asarray(frame.index),K)}
    return DataFrame(data,columns=['date','variable','value'])

df = unpivot(tm.makeTimeDataFrame())
print df

#row colunm values
df_piv = df.pivot('date','variable','value')
print df_piv

a = np.arange(3).repeat(4)
#[0 0 0 0 1 1 1 1 2 2 2 2]
print a