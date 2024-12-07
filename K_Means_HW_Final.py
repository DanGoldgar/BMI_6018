import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Import data into dataframe, replace all '?' values with NaN
arrhythmia_data = pd.read_csv("arrhythmia.data", delimiter=",", header = None)
arrhythmia_data = arrhythmia_data.replace('?',np.nan)
# Replace nan with 0. This is not ideal before normalization however I had trouble getting the mean to work
arrhythmia_data = arrhythmia_data.fillna(0)
print(type(arrhythmia_data))

# Initialize scaler object and normalize data
scaler = StandardScaler()
arrhythmia_data_norm = pd.DataFrame(scaler.fit_transform(arrhythmia_data))

print(arrhythmia_data.head(5))
print(arrhythmia_data_norm.head(5))

# Use PCA to reduce dimensions to 2
pca_num_components = 2
reduced_data = PCA(n_components=pca_num_components).fit_transform(arrhythmia_data_norm)
results = pd.DataFrame(reduced_data,columns=['pca1','pca2'])

# Scatterplot with no clusters.
plt.figure(figsize=(10, 6))
sns.scatterplot(data = results, x = 'pca1', y = 'pca2')
plt.title('No Clusters')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.show()

# Scatterplot with 2 clusters
model = KMeans(n_clusters = 2, random_state = 0, n_init=10)
model.fit(results)

plt.figure(figsize=(10, 6))
sns.scatterplot(data = results, x = 'pca1', y = 'pca2', hue = model.labels_)
plt.plot()
plt.title('2 Clusters')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.show()

# Evaluate squared error for various cluster numbers
K = range(2, 14)
fits = []
score = []

for k in K:
    # train the model for current value of k on training data
    model = KMeans(n_clusters=k, random_state=0, n_init=10).fit(results)

    # append the model to fits
    fits.append(model)

    # Append the silhouette score to scores
    score.append(silhouette_score(results, model.labels_, metric='euclidean'))

# Elbow plot. Here the data does not quite produce the expected elbow shape, however a local minimum is
# observed at 4 clusters. The data will be replotted with this number of clusters
plt.figure(figsize=(10, 6))
sns.lineplot(x = K, y = score)
plt.title('Silhouette Analysis')
plt.show()

# Scatterplot with 4 clusters
model = KMeans(n_clusters = 4, random_state = 0, n_init=10)
model.fit(results)

plt.figure(figsize=(10, 6))
sns.scatterplot(data = results, x = 'pca1', y = 'pca2', hue = model.labels_)
plt.plot()
plt.title('4 Clusters')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.show()