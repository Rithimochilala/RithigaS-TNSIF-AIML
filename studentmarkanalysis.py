import numpy as np

marks = np.array([80, 65, 90, 72, 88, 55, 76, 95, 68, 82])

print("Total marks:", np.sum(marks))
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))

print("Marks greater than 75:")
print(marks[marks > 75])