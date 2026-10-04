import numpy as np

temperature = np.array([28, 31, 33, 29, 35, 32, 27])

print("Average temperature:", np.mean(temperature))
print("Highest temperature:", np.max(temperature))
print("Lowest temperature:", np.min(temperature))

print("Temperatures above 30:")
print(temperature[temperature > 30])

temperature = temperature + 2

print("Updated temperatures:")
print(temperature)