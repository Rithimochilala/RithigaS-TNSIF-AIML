arr = [10, -5, 20, -8, 15, -2]

positive = 0
negative = 0

for i in arr:
    if i > 0:
        positive += i
    elif i < 0:
        negative += i

print("Positive Sum:", positive)
print("Negative Sum:", negative)