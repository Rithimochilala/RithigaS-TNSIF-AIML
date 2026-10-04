from sklearn.tree import DecisionTreeClassifier

# Input data
X = [
    [0, 0],   # Sunny, Hot
    [0, 1],   # Sunny, Cool
    [1, 1],   # Rainy, Cool
    [1, 0],   # Rainy, Hot
    [2, 0],   # Cloudy, Hot
    [2, 1],   # Cloudy, Cool
    [0, 0],   # Sunny, Hot
    [1, 1]    # Rainy, Cool
]

# Output
y = [0, 1, 1, 0, 1, 1, 0, 1]

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Take input
weather = int(input("Enter weather (Sunny=0, Rainy=1, Cloudy=2): "))
temperature = int(input("Enter temperature (Hot=0, Cool=1): "))

# Predict
prediction = model.predict([[weather, temperature]])

if prediction[0] == 1:
    print("Play: Yes")
else:
    print("Play: No")