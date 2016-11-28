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

dataset = randn(25)

# sns.rugplot(dataset)
# plt.hist(dataset,alpha=0.3)
# plt.show()

sns.rugplot(dataset)

m_min= dataset.min()-2
m_max=dataset.max() +2

x_axis = np.linspace(m_min,m_max,100)

bandwidth = ((4*dataset.std()**5) / (3*len(dataset)))**0.2

kernel_list = []

for data_point in dataset:
    #create a kernel for each point and append it to kernel_list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)

    #scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * 0.4

    plt.plot(x_axis,kernel,color='grey',alpha=0.5)

sum_kde = np.sum(kernel_list,axis=0)


sns.kdeplot(dataset)
plt.show()

sns.rugplot(dataset,color='black')

for bw in np.arange(0.5,2,0.25):
    sns.kdeplot(dataset,bw=bw,lw=1.8,label=bw)

plt.show()

kernel_option = ['biw','cos','epa','gau','tri','triw']

for kern in kernel_option:
    sns.kdeplot(dataset,kernel = kern,label=kern)

plt.show()
#vertical axis
#sns.kdeplot(dataset,vertical=True)


#CDF culmulated
sns.kdeplot(dataset,cumulative=True)
plt.show()

mean = [0,0]
cov = [[1,0],[0,100]]

dataset2 = np.random.multivariate_normal(mean,cov,1000)

df = DataFrame(dataset2,columns=['X','Y'])
sns.kdeplot(df)
plt.show()


sns.jointplot('X','Y',df,kind='kde')
plt.show()

