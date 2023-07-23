# -*- coding: utf-8 -*-
"""project file

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MMc02GPcHFjEQFxc7SLLL3WmS_qriBBa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train=pd.read_csv('/content/train-data.csv')
train.head()

train.info()

train.isna().sum()

train.describe()

train.shape

ls=['Name','Location','Fuel_Type','Transmission','Owner_Type']

for i in ls:
  count=train[i].value_counts()
  print('column ',i,'have ',len(count),' unique values')
  print(count.index)
  print('*'*100)

lst=['Location','Fuel_Type','Transmission','Owner_Type']

for i in lst:
  coun=train[i].value_counts()
  plt.bar(coun.index,coun)
  plt.xlabel(i)
  plt.ylabel('count')
  plt.show()

# we should drop columns named - unnamed,newprize,name
# newprize column have large missing value and name have large set of unique values


#get dummies encoding
df1=pd.get_dummies(train[['Location','Fuel_Type','Transmission','Owner_Type']],drop_first=True)
df1

dfe=pd.concat([train,df1],axis=1)
dfe

dfe.columns

# test data file dont have a column named 'Fuel_Type_Electric' therefore we should drop it from the train data
dfe1=dfe.drop(['Unnamed: 0','Name','Location','Fuel_Type','Transmission','Owner_Type','New_Price','Fuel_Type_Electric'],axis=1)

# replace unit from mileage,engine,power

dfe1['Mileage']=dfe1['Mileage'].str.replace('km/kg','')
dfe1['Mileage']=dfe1['Mileage'].str.replace('kmpl','')
dfe1['Engine']=dfe1['Engine'].str.replace('CC','')
dfe1['Power']=dfe1['Power'].str.replace('bhp','')

# there is 'null' in engine,power,mileage given in description

dfe1['Mileage']=dfe1['Mileage'].str.replace('null','0')
dfe1['Engine']=dfe1['Engine'].str.replace('null','0')
dfe1['Power']=dfe1['Power'].str.replace('null','0')

dfe1

dfe1.dtypes

# uint8 un directional integer

# convert datatype of object into int

dfe1['Engine']=dfe1['Engine'].astype(float)
dfe1['Mileage']=dfe1['Mileage'].astype(float)
dfe1['Power']=dfe1['Power'].astype(float)
dfe1.dtypes

dfe1.isna().sum()

# consider the '0' value we give instead of 'null' as a missing value and replace with NaN
dfe1.loc[dfe1.Engine==0,'Engine']=np.NaN
dfe1.loc[dfe1.Mileage==0,'Mileage']=np.NaN
dfe1.loc[dfe1.Power==0,'Power']=np.NaN

dfe1.isna().sum()

# filling missing value

dfe1['Mileage']=dfe1['Mileage'].fillna(dfe1['Mileage'].mean())
dfe1['Engine']=dfe1['Engine'].fillna(dfe1['Engine'].mean())
dfe1['Power']=dfe1['Power'].fillna(dfe1['Power'].mean())
dfe1['Seats']=dfe1['Seats'].fillna(dfe1['Seats'].mode()[0])

dfe1.isna().sum()

x=dfe1.drop(['Price'],axis=1)
y=dfe1['Price']

# loading test dataset and do the preproccessing

test=pd.read_csv('/content/test-data.csv')
test.head()

test.info()

test.describe()

test.isna().sum()

lst=['Location','Fuel_Type','Transmission','Owner_Type']

for i in lst:
  coun=test[i].value_counts()
  plt.bar(coun.index,coun)
  plt.xlabel(i)
  plt.ylabel('count')
  plt.show()

# encoding using get dummies

ts=pd.get_dummies(test[['Location','Fuel_Type','Transmission','Owner_Type']],drop_first=True)
ts

tst=pd.concat([test,ts],axis=1)
tst

tst1=tst.drop(['Unnamed: 0','Name','Location','Fuel_Type','Transmission','Owner_Type','New_Price'],axis=1)
tst1

# removing the unit portion from the data

tst1['Mileage']=tst1['Mileage'].str.replace('km/kg','')
tst1['Mileage']=tst1['Mileage'].str.replace('kmpl','')
tst1['Engine']=tst1['Engine'].str.replace('CC','')
tst1['Power']=tst1['Power'].str.replace('bhp','')

# there is 'null' in engine,power,mileage given in description

tst1['Mileage']=tst1['Mileage'].str.replace('null','0')
tst1['Engine']=tst1['Engine'].str.replace('null','0')
tst1['Power']=tst1['Power'].str.replace('null','0')

tst1.dtypes

# convert datatype of object into int
tst1['Engine']=tst1['Engine'].astype(float)
tst1['Mileage']=tst1['Mileage'].astype(float)
tst1['Power']=tst1['Power'].astype(float)
tst1.dtypes

# consider the '0' value we give instead of 'null' as a missing value and replace with NaN
tst1.loc[tst1.Engine==0,'Engine']=np.NaN
tst1.loc[tst1.Mileage==0,'Mileage']=np.NaN
tst1.loc[tst1.Power==0,'Power']=np.NaN

tst1.isna().sum()

# filling missing values

tst1['Mileage']=tst1['Mileage'].fillna(tst1['Mileage'].mean())
tst1['Engine']=tst1['Engine'].fillna(tst1['Engine'].mean())
tst1['Power']=tst1['Power'].fillna(tst1['Power'].mean())
tst1['Seats']=tst1['Seats'].fillna(tst1['Seats'].mode()[0])

tst1.isna().sum()

z=tst1

# model creation
from sklearn.linear_model import LinearRegression
ln=LinearRegression()
ln.fit(x,y)
ln.predict(z)