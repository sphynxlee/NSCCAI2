import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate a synthetic dataset
np.random.seed(42)
X = np.random.rand(100, 10)  # 100 samples, 10 features
y = np.random.randint(2, size=100)  # Binary labels (0 or 1)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a DMatrix, which is an optimized data structure for XGBoost
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Set parameters for XGBoost
params = {
    'max_depth': 3,  # Maximum depth of a tree
    'eta': 0.1,  # Learning rate
    'objective': 'binary:logistic',  # Objective function for binary classification
    'eval_metric': 'logloss'  # Evaluation metric
}

# Train the model
num_round = 100  # Number of boosting rounds
bst = xgb.train(params, dtrain, num_round)

# Make predictions
preds = bst.predict(dtest)
# Convert probabilities to binary predictions
predictions = [1 if p > 0.5 else 0 for p in preds]

# Evaluate the accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')

# Feature importance (optional)
import matplotlib.pyplot as plt
xgb.plot_importance(bst)
plt.show()
