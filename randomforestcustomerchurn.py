import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Input data
X = np.array([
    [22, 2, 500],
    [25, 5, 600],
    [30, 1, 800],
    [35, 8, 550],
    [40, 10, 500],
    [28, 3, 900],
    [45, 12, 650],
    [32, 2, 850]
])

# Output data
y = np.array([1, 0, 1, 0, 0, 1, 0, 1])

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X, y)

# New customer
age = int(input("Enter age: "))
tenure = int(input("Enter tenure: "))
bill = int(input("Enter monthly bill: "))

# Predict
prediction = model.predict([[age, tenure, bill]])

if prediction[0] == 1:
    print("Customer will Leave")
else:
    print("Customer will Stay")