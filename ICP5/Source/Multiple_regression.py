import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

#Loading the data
data= pd.read_csv('winequality-red.csv')
##Null values
nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)
#Finding correlation with the target class
numeric_features = data.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['quality'].sort_values(ascending=False)[1:4], '\n')
#Dropping the columns having less correlation with target class
train_dt = data.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(train_dt.isnull().sum() != 0))
#Splitting data
y = np.log(data.quality)
X = train_dt.drop(['quality'], axis=1)
X_train, X_test,y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=42)
#creation of regression model and training it and predicting the target
model=LinearRegression().fit(X_train,y_train)
predict=model.predict(X_test)
#evaluation of model using metrics
MSE = mean_squared_error(y_test, predict)
r2_score = r2_score(y_test,predict)
print("Mean squared error :",MSE)
print("R2 score : ",r2_score)