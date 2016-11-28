import numpy as np
import pandas as pd
from pandas import Series,DataFrame

df = DataFrame({'city':['Alma','Brian head','fox park'],
                'altitude':[3158,300,2762]})

print df

state_map={'Alma':'Colorado','Brian head':'Utah','fox park':'Wyoming'}

df['state']=df['city'].map(state_map)

print df