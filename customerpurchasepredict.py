import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Dataset
X = np.array([
    [20, 15000],
    [22, 18000],
    [25, 22000],
    [28, 30000],
    [30, 35000],
    [32, 40000],
    [35, 45000],
    [38, 50000],
    [40, 55000],
    [45, 60000]
])

# Output
y = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Logistic Regression
logistic = LogisticRegression()
logistic.fit(X_train, y_train)

# Decision Tree
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

# New customer
new_customer = [[27, 28000]]

# Predictions
logistic_prediction = logistic.predict(new_customer)
tree_prediction = tree.predict(new_customer)

print("Logistic Regression Prediction:", logistic_prediction[0])
print("Decision Tree Prediction:", tree_prediction[0])

# Test predictions
logistic_test = logistic.predict(X_test)
tree_test = tree.predict(X_test)

# Accuracy
logistic_accuracy = accuracy_score(y_test, logistic_test)
tree_accuracy = accuracy_score(y_test, tree_test)

print("Logistic Regression Accuracy:", logistic_accuracy)
print("Decision Tree Accuracy:", tree_accuracy)