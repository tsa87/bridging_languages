def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr)-1)

def quick_sort_helper(arr, low, high):
    if low < high:
        pivot_point = partition(arr, low, high)
        quick_sort_helper(arr, low, pivot_point-1)
        quick_sort_helper(arr, pivot_point, high)
    return arr

def partition(arr, low, high):
    pivot_value = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot_value:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
