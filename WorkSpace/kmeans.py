import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


df = pd.DataFrame({
    'x': [1999, 2015, 2014, 2003, 2005, 2007, 2008, 2012, 2016, 2011, 2012, 1998, 2004, 2006, 2000,  2009, 2010, 2012, 2017],
    'y': [5.0, 4.5, 5.8, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2, 4.7, 3.5, 5.4, 6.3, 5.2, 4.1, 5.4, 4.9, 5.1, 4.6]
})

np.random.seed(100)
k = 2
centroids = {
    i + 1: [np.random.randint(0, 100), np.random.randint(0, 100)]
    for i in range(k)
}

fig = plt.figure(figsize=(6, 6))
plt.scatter(df['x'], df['y'], color='b')
colmap = {1: 'r', 2: 'r', 3: 'r'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i],edgecolors="r")
plt.xlim(1999, 2017)
plt.ylim(3, 7)
plt.show()