import numpy as np
import matplotlib.pyplot as plt

X = np.array([
       [1.22831184, -0.75717844],
       [0.69840909, -1.38029525],
       [2.54881729, 2.50225822],
])
# X[:, 0], X[:, 1]
# print(X[:, 0])
# print(X[:, 1])

plt.scatter(X[:, 0], X[:, 1], cmap='viridis')
ax = plt.gca()
ax.set_aspect('equal')
plt.show()