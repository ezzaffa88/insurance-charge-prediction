import pandas as pd
import numpy as np
from sklearn import linear_model
df = pd.read_csv('insurance.csv')

df.drop('region',axis=1,inplace=True)
male = pd.get_dummies(df['sex'],drop_first = True)
df.drop('sex', axis=1, inplace=True)
df = pd.concat([df, male], axis=1)
df.smoker.replace(('yes', 'no'), (1, 0), inplace=True)
y=df['charges'].values
X=df.drop(['charges'],axis=1).values
rg = linear_model.LinearRegression()

rg.fit(df[['age','bmi','children','smoker','male']],df.charges)
rg.coef_
rg.intercept_
#test prediction
print(rg.predict([[69,29.0,0,1,0]]))

import pickle
pickle.dump(rg, open('Insurance_charge_prediction.pkl', 'wb'))