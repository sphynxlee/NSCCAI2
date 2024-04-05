# XGBoost stands for eXtreme Gradient Boosting, which is an optimized distributed gradient boosting library designed to be highly efficient, flexible, and portable.
# It's widely used for supervised learning problems, particularly in structured/tabular data,
# and has proven to be highly effective in various machine learning competitions and real-world applications.

## reference: https://www.datacamp.com/tutorial/xgboost-in-python

import numpy as np
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert data into DMatrix format, which is a XGBoost-specific optimized data structure
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Parameters for XGBoost model
params = {
    # Maximum depth of a tree
    'max_depth': 3,
    # Learning rate
    'eta': 0.1,
    # Objective function for multiclass classification
    'objective': 'multi:softmax',
    # Number of classes
    'num_class': 3,
    # Evaluation metric
    'eval_metric': 'merror'
}

# Train the XGBoost model
num_rounds = 100
model = xgb.train(params, dtrain, num_rounds)

# Predict on test set
y_pred = model.predict(dtest)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
