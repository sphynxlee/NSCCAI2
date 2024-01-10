import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

np.random.seed(0)

# Create sunny data
sunny_data = 20 + 10 * np.random.randn(100, 2)

# cloudy data
cloudy_data = 50 + 10 * np.random.randn(100, 2)

# rainy data
rainy_data = 80 + 10 * np.random.randn(100, 2)

# snowy data
snowy_data = 110 + 10 * np.random.randn(100, 2)

# Combine all weather data
weather_data = np.vstack([sunny_data, cloudy_data, rainy_data, snowy_data])

model = KMeans(n_clusters=4, random_state=42)
model.fit(weather_data)

# Get cluster centers and labels
centers = model.cluster_centers_
labels = model.labels_

# Plotting the data points and cluster centers
plt.scatter(weather_data[:, 0], weather_data[:, 1], c=labels)
plt.title('KMeans Clustering of Weather Data')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.show()
