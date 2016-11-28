import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt

#pivot table

from StringIO import StringIO
data='''\
Sample Animal Intelligence
1 Dog Smart
2 Dog Smart
3 Cat Dumb
4 Cat Dumb
5 Dog Dumb
6 Cat Smart '''

df = pd.read_table(StringIO(data),sep='\s+')

print df

#count frequcy
print pd.crosstab(df.Animal,df.Intelligence,margins=True)