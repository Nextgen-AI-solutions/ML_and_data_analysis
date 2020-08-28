import pickle
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures as pol

poly=pol(degree=7)
model=pickle.load(open('model.pickle','rb'))
#create function to set a date upto predictions need to be done
def ent_date(yyyy=int(input('Year in format yyyy : ')),
    mm=int(input('month in format mm : ')),
    dd=int(input('days in format dd : '))):
        d = dt.date(yyyy,mm,dd)
        return d
    
d = ent_date()

pre_date=dt.date(2020,7,21)


# date range upto predictions has to be done

y = d - pre_date
print(y)
# converting timedealat to float

y = y/dt.timedelta(days=1)
newdtr = int(y/1)

# pred=int(abs(model.predict(poly.fit_transform([[156]]))))
# print(pred)

newcases=[]

def crtlst(y):
    for i in range(141,141+newdtr):
        p = int(abs(model.predict(poly.fit_transform([[i]]))))
        newcases.append(p)
        

crtlst(newdtr)

# create a data frame to showcase predicted values

dates = pd.date_range('7/22/2020',periods=newdtr,freq='D')
datf = pd.DataFrame(data=newcases,columns=['cases'])
datf['Dates'] = dates
datf = datf[['Dates','cases']]
print(datf)

#plot the data

x=datf['Dates']
y=datf['cases']
plt.plot(x,y,'b')
plt.xlabel('days')
plt.ylabel('predicted_cases')
plt.plot()
plt.show()
print(datf.head(60))
