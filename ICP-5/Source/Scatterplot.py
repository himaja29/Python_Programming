import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
data = pd.read_csv('train .csv')
data = pd.read_csv('train .csv', sep=',',usecols=(62,80))
y = data['SalePrice']
X = data['GarageArea']
print('Data size before deleting outliers',data.shape)
plt.scatter(X,y)
plt.title("Scatter plot before deleting outliers")
plt.ylabel("SalesPrice")
plt.xlabel("GarageArea")
plt.show()

#Finging the outliers using Z-score
#Data points with Z-score greater than three are considered as outliers
data = data[data['GarageArea']>200]
z = np.abs(stats.zscore(data))
threshold = 3
modified_data = data[(z < 3).all(axis=1)]
y = modified_data['SalePrice']
x = modified_data['GarageArea']
print('Data size after deleting outliers : ',modified_data.shape)
plt.scatter(x,y)
plt.title("Scatter plot after deleting outliers")
plt.ylabel("SalesPrice")
plt.xlabel("GarageArea")
plt.show()