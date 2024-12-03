import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Import data into dataframe
arrhythmia_data = pd.read_csv("arrhythmia.data", delimiter=",", header = None)
# Slice a 2d section of data. Here we choose the columns for age and QRS duration
arrhythmia_data_2D = arrhythmia_data.iloc[:,[0,4]]

print(arrhythmia_data_2D.head(5))

# Scatterplot with no clusters. The distribution of data is acceptable and so we skip normalization step
plt.figure(figsize=(10, 6))
sns.scatterplot(data = arrhythmia_data_2D, x = 0, y = 4)
plt.title('No Clusters')
plt.xlabel('Age')
plt.ylabel('QRS Duration')

plt.show()

# Scatterplot with 2 clusters
model = KMeans(n_clusters = 2, random_state = 0, n_init=10)
model.fit(arrhythmia_data_2D)

plt.figure(figsize=(10, 6))
sns.scatterplot(data = arrhythmia_data_2D, x = 0, y = 4, hue = model.labels_)
plt.plot()
plt.title('2 Clusters')
plt.xlabel('Age')
plt.ylabel('QRS Duration')
plt.show()

K = range(2, 14)
fits = []
score = []

for k in K:
    # train the model for current value of k on training data
    model = KMeans(n_clusters=k, random_state=0, n_init=10).fit(arrhythmia_data_2D)

    # append the model to fits
    fits.append(model)

    # Append the silhouette score to scores
    score.append(silhouette_score(arrhythmia_data_2D, model.labels_, metric='euclidean'))

# Elbow plot. Here the data does not produce the expected elbow shape, however a minimum is
# observed at 6 clusters. The data will be replotted with this number of clusters
plt.figure(figsize=(10, 6))
sns.lineplot(x = K, y = score)
plt.title('Silhouette Analysis')
plt.show()

# Scatterplot with 6 clusters
model = KMeans(n_clusters = 2, random_state = 0, n_init=10)
model.fit(arrhythmia_data_2D)

plt.figure(figsize=(10, 6))
sns.scatterplot(data = arrhythmia_data_2D, x = 0, y = 4, hue = model.labels_)
plt.plot()
plt.title('6 Clusters')
plt.xlabel('Age')
plt.ylabel('QRS Duration')
plt.show()