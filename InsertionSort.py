# Time complexity.
# Best case: O(n)
# Worst case: O(n2)
# Average case: O(n2)
# Space complexity: O(1)
# Usecase:
#   + Elements in array is small.
#   + Array is almost sorted, several elements are not sorted.
# Optimize with Binary Insertion Sort - using Binary Search
import profile
from read_sample import ReadSampleData

def InsertionSortAsc(arr):
    i = 0
    while i < len(arr):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        i += 1

def InsertionSortDesc(arr):
    i = 0
    while i < len(arr):
        for j in range(i, 0, -1):
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        i += 1

def BinaryInsertionSort(arr):
    i = 0
    left = 0
    while i < len(arr):
        right = arr[i]
        for j in range()
        i += 1

if __name__ == "__main__":
    arr = ReadSampleData()
    print(arr)
    # Insertion sort Asc
    profile.run('InsertionSortDesc(arr); print()')
    print(arr)