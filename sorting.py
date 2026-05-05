arr = [50, 20, 40, 10, 30]

# Bubble
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Bubble:", arr)

# Selection
arr = [50, 20, 40, 10, 30]
for i in range(len(arr)):
    min_i = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_i]:
            min_i = j
    arr[i], arr[min_i] = arr[min_i], arr[i]

print("Selection:", arr)
print("Top 5:", sorted(arr, reverse=True)[:5])
