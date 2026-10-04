a = [10, 20, 10, 30, 20, 10]

max_count = 0
max_number = 0

for i in a:
    count = 0

    for j in a:
        if i == j:
            count += 1

    if count > max_count:
        max_count = count
        max_number = i

print(max_number)