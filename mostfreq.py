arr = [2, 5, 2, 8, 5, 2, 3, 5, 2]

max_count = 0
most_frequent = 0

for i in arr:
    count = 0

    for j in arr:
        if i == j:
            count += 1

    if count > max_count:
        max_count = count
        most_frequent = i

print("Most Frequent Element:", most_frequent)
print("Frequency:", max_count)