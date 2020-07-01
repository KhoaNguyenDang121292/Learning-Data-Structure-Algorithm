"""
    KEY CONCEPT:
        1. Find pivot with Partition algorithm
        2. Quick sort for left half (from low to pivot) and right half (pivor to high)
"""
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high, +1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

# def quickSort(arr):
#     pivot = arr[len(arr)-1]
#     i = -1
#     j = 0
#     while i < len(arr) and j < len(arr):
#         if arr[i] <= pivot:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#         j += 1

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        print("Pivot element: " + str(arr[pivot]))
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot, high)

if __name__ == "__main__":
    import sys
    sys.path.append("D:/DSaAlgo")

    from read_sample import ReadSampleData
    arr = ReadSampleData()
    print("Array before quick sort: " + str(arr))
    quickSort(arr, 0, len(arr)-1)
    print("Array after quick sort: " + str(arr))