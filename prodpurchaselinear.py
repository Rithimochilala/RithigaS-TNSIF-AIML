import numpy as np
from sklearn.linear_model import LogisticRegression

# Input data
X = np.array([
    [20, 15000],
    [22, 18000],
    [25, 25000],
    [28, 30000],
    [30, 35000],
    [35, 40000],
    [40, 50000],
    [45, 60000]
])

# Output data
y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Take input from user
age = int(input("Enter age: "))
income = int(input("Enter income: "))

# Predict
prediction = model.predict([[age, income]])

if prediction[0] == 1:
    print("Purchased: Yes")
else:
    print("Purchased: No")