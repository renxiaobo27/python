import numpy as np
import pandas as pd
from pandas import Series,DataFrame

np.random.seed(12345)


df = DataFrame(np.random.randn(1000,4))

print df.head()

print df.tail()

print df.describe()

col = df[0]

print col.head()

print col[np.abs(col)>3]

#any col return that row
print df[(np.abs(df)>3).any(1)]

df[np.abs(df)>3] = np.sign(df)*3