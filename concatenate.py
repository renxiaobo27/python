import numpy as np
import pandas as pd
from pandas import Series,DataFrame

arr1 = np.arange(9).reshape(3,3)
print arr1

print np.concatenate([arr1,arr1],axis=0)

print np.concatenate([arr1,arr1],axis=1)

ser1 = Series([0,1,2],index=['T','U','V'])
ser2 = Series([3,4],index=['X','Y'])

print pd.concat([ser1,ser2])

print pd.concat([ser1,ser2],axis=1)

print pd.concat([ser1,ser2],keys=['cat1','cat2'])


df1 = DataFrame(np.random.randn(4,3),columns=['X','Y','Z'])

df2 = DataFrame(np.random.randn(3,3),columns=['Y','Q','X'])

print pd.concat([df1,df2])

print pd.concat([df1,df2],ignore_index=True)