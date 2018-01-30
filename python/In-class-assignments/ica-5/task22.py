# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

height = np.array([5.0,50,5.0,5.0,5.4,5.4,5.4,5.4,5.4,5.6,5.6,5.6,5.6,6.0,6.0,6.0,6.0,])
weight = np.array([50,54,58,60,62,64,65,66,70,72,74,76,80,82,84,86,88])
size = np.array([0,0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3])
dataset = np.column_stack((height,weight,size))

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(dataset)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(dataset)

# Visualising the clusters
plt.scatter(dataset[y_kmeans == 0, 0], dataset[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(dataset[y_kmeans == 1, 0], dataset[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(dataset[y_kmeans == 2, 0], dataset[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(dataset[y_kmeans == 3, 0], dataset[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of tshirts')
plt.xlabel('')
plt.ylabel('')
plt.legend()
plt.show()
