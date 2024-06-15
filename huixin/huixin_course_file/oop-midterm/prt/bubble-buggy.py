def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n):  # Corrected the range
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]  # Corrected the swapping
    return arr

print(bubble_sort([4, 2, 1, 8, 7, 6]))
