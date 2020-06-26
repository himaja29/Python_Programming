import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('CC.csv')
print(data["TENURE"].value_counts())

#null values
nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns  = ['Null Count']
nulls.index.name  = 'Feature'
print(nulls)

#Remove any null values by the mean
data.loc[(data['MINIMUM_PAYMENTS'].isnull()==True),'MINIMUM_PAYMENTS']=data['MINIMUM_PAYMENTS'].mean()
data.loc[(data['CREDIT_LIMIT'].isnull()==True),'CREDIT_LIMIT']=data['CREDIT_LIMIT'].mean()

x = data.iloc[:,1:-1]
y = data.iloc[:,-1]
print(x.shape,y.shape)

#elbow method to know the number of clusters
#wcss -within cluster sum of squares
wcss = []
for i in range(1,7):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
print(wcss)
plt.plot(range(1,7),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()


#nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=3)
km.fit(x)
y_cluster_kmeans= km.predict(x)
from sklearn import metrics
silhouette_score = metrics.silhouette_score(x, y_cluster_kmeans)
print("silhouette_score is ",silhouette_score)

# standardization
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x)

# Apply transform to both the training set and the test set.
x_scaler = scaler.transform(x)
pca = PCA(3)
x_pca = pca.fit_transform(x_scaler)
df2 = pd.DataFrame(data=x_pca)
final_data = pd.concat([df2,data[['TENURE']]],axis=1)
print(final_data)

# KMeans after standarization

km = KMeans(n_clusters=3)
km.fit(x_scaler)
y_cluster_kmeans= km.predict(x_scaler)
from sklearn import metrics
After_score = metrics.silhouette_score(x_scaler, y_cluster_kmeans)
print("silhouette_score after scaling:",After_score)

#bonus
pca= PCA(3)
x_pca = pca.fit_transform(x_scaler)

km.fit(x_pca)
y_cluster_kmeans= km.predict(x_pca)
PCA_score = metrics.silhouette_score(x_pca, y_cluster_kmeans)
print("silhouette score after applying PCA ",PCA_score)

#visualizing the clustering of the result
colors = ["red", "blue", "green"]
for i in range(3):
    x_axis = x_pca[y_cluster_kmeans == i][:,0]
    y_axis = x_pca[y_cluster_kmeans == i][:,1]
    plt.scatter(x_axis,y_axis,color=colors[i])
plt.show()
