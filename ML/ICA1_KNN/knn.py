import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.markers import MarkerStyle
from sklearn.model_selection import train_test_split

# Generate a synthetic rain forecast dataset
np.random.seed(42)
temperature = np.random.uniform(10, 30, 100)
humidity = np.random.uniform(30, 80, 100)
# 1 indicates rain, 0 indicates no rain
labels = np.where((temperature > 20) & (humidity > 50), 1, 0)

# Split the dataset into training and testing sets
weather_datasets = np.column_stack((temperature, humidity))
train_data = weather_datasets[:80]
train_labels = labels[:80]
test_data = weather_datasets[80:]
test_labels = labels[80:]

def euclidean_distance(v1,v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    distance = np.sqrt(np.sum((v1-v2)**2))
    return(distance)

class KNN:
    def __init__(self,k=3):
        self.k = k
        self.points = None

    def fit(self, points):
        self.points = points

    def predict(self, new_point):
        if self.points is None:
            print("Error: Model not fitted.")
            return None

        distances = []

        for category in self.points:
            for point in self.points[category]:
                distance = euclidean_distance(new_point,point)
                distances.append([distance,category])

        categories = [category[1] for category in sorted(distances)[:self.k]]
        print("Categories",categories)
        result = Counter(categories).most_common(1)[0][0]
        # result = Counter(categories).most_common(1)
        print("Result",result)
        return(result)

# Create a KNN instance, fit the model with training data, and make predictions
knn_weather = KNN(k=3)
# knn_weather.fit({0: X_train[y_train == 0], 1: X_train[y_train == 1]})
knn_weather.fit({0: train_data[train_labels == 0], 1: train_data[train_labels == 1]})
new_point_weather = [25, 60]
predicted_category_weather = knn_weather.predict(new_point_weather)

plt.scatter(train_data[train_labels == 0][:, 0], train_data[train_labels == 0][:, 1], label='No Rain', color='blue')
plt.scatter(train_data[train_labels == 1][:, 0], train_data[train_labels == 1][:, 1], label='Rain', color='orange')
plt.scatter(new_point_weather[0], new_point_weather[1], color='red' if predicted_category_weather == 1 else 'blue', marker=MarkerStyle("*"), s=200, zorder=100)
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.legend()
plt.show()