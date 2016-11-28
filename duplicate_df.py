import numpy as np
import pandas as pd
from pandas import Series,DataFrame


df = DataFrame({'key1':['A']*2+['B']*3,
                'key2':[2,2,3,3,3]})

print df

print df.duplicated()

print df.drop_duplicates()

print df.drop_duplicates(['key1'])

print df.drop_duplicates(['key1'],take_last=True)