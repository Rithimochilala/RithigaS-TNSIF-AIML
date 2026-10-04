arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = arr[0]
current_sum = 0

start = 0
end = 0

for i in range(len(arr)):
    current_sum = 0

    for j in range(i, len(arr)):
        current_sum += arr[j]

        if current_sum > max_sum:
            max_sum = current_sum
            start = i
            end = j

print("Maximum Subarray Sum:", max_sum)
print("Subarray:", arr[start:end + 1])