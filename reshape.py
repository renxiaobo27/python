import numpy as np
import pandas as pd
from pandas import Series,DataFrame


df = DataFrame(np.arange(8).reshape(2,4),index=pd.Index(['LA','SF'],name='city'),columns=
               pd.Index(['A','B','C','D'],name='letter'))

print df


df_st = df.stack()

print df_st

print df_st.unstack()

print df_st.unstack('city')


#handle nan value

ser1 = Series([0,1,2],index=['Q','X','Y'])
ser2 = Series([4,5,6],index=['X','Y','Z'])

ser3 = pd.concat([ser1,ser2],keys=['Alpha','Beta'])
print ser3
print ser3.unstack()
#no nan value any more
print ser3.unstack().stack()

df3 = ser3.unstack()
print df3
#keep nan
print df3.stack(dropna=False)