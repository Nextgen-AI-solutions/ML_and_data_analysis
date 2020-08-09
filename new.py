import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Covid.csv')
df=df[['Date','cases']]
df.dropna(inplace=True)
df['next_day_cases']=df['cases'].shift(+1)
df['daily_cases']=df['cases']-df['next_day_cases']
df=df.iloc[5:,:]
df=df[['Date','cases','daily_cases']]
df.set_index('Date',inplace=True)
print(df)  
xs=df.index
ys=df['cases']
ys2=df['daily_cases']
#creating plots to visualize data
plt.subplot(3,2,1)
plt.plot(xs,ys,'r')
plt.xlabel('Date')
plt.title('Total_Cases')
plt.subplot(3,2,2)
plt.plot(xs,ys2,'g.')
plt.xlabel('Date')
plt.title('Daily_Cases')
ax1=plt.subplot(3,1,3)
ax2=ax1.twinx()
curve1=ax1.plot(xs,ys,'r',label='Total_Cases')
curve2=ax2.plot(xs,ys2,'b',label='Daily_Cases')
plt.title('Total cases & daily cases')
plt.rcParams['figure.figsize']=(15,10)
plt.show()

