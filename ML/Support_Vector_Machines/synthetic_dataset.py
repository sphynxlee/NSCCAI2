from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# Generate a synthetic dataset with 2 features and 2 classes
X, y = make_classification(
    n_samples=100,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_classes=2,
    n_clusters_per_class=1,
    random_state=42
)

# Plot the synthetic dataset
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')  # You can choose any other colormap here
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Synthetic Classification Dataset')
plt.show()
