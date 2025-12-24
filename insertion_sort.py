# Insertion Sort implementation

arr = [5, 3, 4, 1]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    # Shift elements greater than key
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Sorted list:", arr)
