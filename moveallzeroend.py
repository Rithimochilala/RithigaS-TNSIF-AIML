a = [10, 0, 20, 0, 30, 40]

b = []

for i in a:
    if i != 0:
        b.append(i)

for i in a:
    if i == 0:
        b.append(i)

print(b)