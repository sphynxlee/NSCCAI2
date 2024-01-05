import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

#https://www.geogebra.org/
points = {"red": [[2,4],[1,3],[2,3],[3,2],[2,1]],
          "blue": [[5,6],[4,5],[4,6],[6,6],[5,4]]}



new_point = [3,4]


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


myKNN = KNN()
myKNN.fit(points)
new_category = myKNN.predict(new_point)
print(new_category)

ax = plt.subplot()
ax.grid(True,color="#323232")
ax.figure.set_facecolor("#121212")
ax.tick_params(axis="x",color="white")
ax.tick_params(axis="y",color="white")

for point in points['blue']:
    ax.scatter(point[0],point[1],color="#0000FF",s=68)

for point in points['red']:
    ax.scatter(point[0],point[1],color="#FF0000",s=68)

ax.scatter(new_point[0],new_point[1], color=new_category, marker="*",s=200,zorder=100)

plt.show()






