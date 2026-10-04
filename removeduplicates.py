arr = [10, 20, 10, 30, 20, 40, 30]

new = []

for i in arr:
    if i not in new:
        new.append(i)

print(new)