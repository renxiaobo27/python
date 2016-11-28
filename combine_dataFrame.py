import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser1 = Series([2,np.nan,4,np.nan,6,np.nan],index = ['Q','R','S','T','U','V'])

ser2 = Series(np.arange(len(ser1)),dtype=np.float64,index=['Q','R','S','T','U','V'])


print ser1
print ser2


ser3 = Series(np.where(pd.isnull(ser1),ser2,ser1),index = ser1.index)

#short cut
ser1.combine_first(ser2)

nan = np.nan
df1 = DataFrame({'X':[1.,np.nan,3.,nan],'Y':[nan,5.,nan,7.],'Z':[nan,9,nan,11]})
df2 = DataFrame({'X':[2.,4.,nan,6.,8.],'Y':[nan,10.,12,14.,16.]})

print df1
print df2
df3 = df1.combine_first(df2)
print df3