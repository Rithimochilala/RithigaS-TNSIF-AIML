arr = [1, 2, 3, 5, 6, 7]

n = 7

total = 0
for i in range(1, n + 1):
    total += i

arr_sum = 0
for i in arr:
    arr_sum += i

missing = total - arr_sum

print("Missing Number:", missing)