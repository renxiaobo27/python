import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

#stats
from scipy import  stats

#plot
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

flight_df = sns.load_dataset('flights')

print flight_df.head()

#row col data
flight_df = flight_df.pivot('month','year','passengers')
print flight_df.head()

sns.heatmap(flight_df)
plt.show()

#number
sns.heatmap(flight_df,annot=True,fmt='d')
plt.show()

#set center
sns.heatmap(flight_df,center=flight_df.loc['January',1955])
plt.show()

f,(axis1,axis2) = plt.subplots(2,1)

yearly_flight = flight_df.sum()

years = pd.Series(yearly_flight.index.values)
years = pd.DataFrame(years)

flights = pd.Series(yearly_flight.values)
flights = pd.DataFrame(flights)

year_df = pd.concat((years,flights),axis=1)
year_df.columns = ['Year','Flights']

sns.barplot('Year',y='Flights',data=year_df,ax=axis1)

sns.heatmap(flight_df,cmap='Blues',ax=axis2,cbar_kws={'orientation':'horizontal'})
plt.plot()

