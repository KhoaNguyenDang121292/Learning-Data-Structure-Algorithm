# Best case: array is sorted - O(n)
# Worst case: O(n2)
# Average case: O(n2)
# Time complexity: O(n2)
# Space complexity: O(1)

import tracemalloc
import cProfile
from read_sample import ReadSampleData

def SelectionSortAsc(arr):
    i = 0
    while i <= len(arr) - 1:
        minPos = i
        for j in range(i+1, len(arr), +1):
            if arr[j] < arr[minPos]:
                arr[j], arr[minPos] = arr[minPos], arr[j]
        i += 1

def SelectionSortDesc(arr):
    i = 0
    while i <= len(arr) - 1:
        maxPos = i
        for j in range(i+1, len(arr), +1):
            if arr[j] > arr[maxPos]:
                arr[j], arr[maxPos] = arr[maxPos], arr[j]
        i += 1

# Idea is get minPos and maxPos at the same time and place
#   them in right position.
def SelectionSortOptimize_1(arr):
    i = 0
    while i <= len(arr) - 1:
        minPos = i
        maxPos = i
        for j in range(i+1, len(arr), +1):
            if arr[j] < arr[minPos]:
                arr[j], arr[minPos] = arr[minPos], arr[j]
            if arr[len(arr)-1] < arr[maxPos]:
                arr[len(arr)-1], arr[maxPos] = arr[maxPos], arr[len(arr)-1]
        i += 1

if __name__ == "__main__":
    tracemalloc.start()
    arr = ReadSampleData()
    SelectionSortAsc(arr)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    print(arr)