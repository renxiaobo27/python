import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt

df_wine = pd.read_csv('whitewines.csv',sep=',')

print df_wine.head()


def ranker(df):
    df['alc_content_rank'] = np.arange(len(df))+1
    return df

df_wine.sort('alcohol',ascending = False,inplace=True)

df_wine = df_wine.groupby('quality').apply(ranker)

print df_wine.head()


num_of_qual = df_wine['quality'].value_counts()
print num_of_qual

print df_wine[df_wine.alc_content_rank==1].head(len(num_of_qual))