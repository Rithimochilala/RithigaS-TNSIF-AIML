arr = [10, 20, 30, 40, 50]

reverse = []

for i in range(len(arr) - 1, -1, -1):
    reverse.append(arr[i])

print(reverse)