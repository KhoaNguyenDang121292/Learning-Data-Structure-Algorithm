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

def InsertionSortAscOptimize(arr, start, end):
    i = start
    while i < end:
        for j in range(i, start, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        i += 1

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

def BinarySearch(arr, k):
    left = 0
    right = len(arr) - 1
    mid = 0
    while left <= right:
        mid = (left + right)//2
        if arr[mid] < k:
            left = mid + 1
        elif arr[mid] > k:
            right = mid - 1
        else:
            return mid if mid > 0 else 0
    print(str(left) + " - " + str(mid) + " - " + str(right))
    return 0

def BinaryInsertionSort(arr):
    i = 1
    while i < len(arr):
        # Find position where left = mid = right
        pos = BinarySearch(arr[:i-1], arr[i])
        # print(pos)
        # Sort array with InsertionSort: from pos to i
        InsertionSortAscOptimize(arr, pos, i)
        # print(arr[pos:i])
        # print("Element: " + str(arr[i]) + " - position: " + str(pos))
        i += 1

if __name__ == "__main__":
    arr = ReadSampleData()
    print(arr)
    # Insertion sort Asc
    profile.run('BinaryInsertionSort(arr); print()')
    # print(arr)