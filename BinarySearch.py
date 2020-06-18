# Best case: 
# Worst case:
# Average case:
# Time complexity: O(log2(n))
# Space complexity:
import tracemalloc
from read_sample import ReadSampleData

def BinarySearch(arr, k):
    left = 0
    right = len(arr) - 1
    mid = (left + right)//2
    i = 0
    while i < len(arr):
        if k > arr[mid]:
            left = mid + 1
        if k < arr[mid]:
            right = mid - 1
        mid = (left + right)//2
        if k == arr[mid]:
            return mid
        i += 1
    return -1

if __name__ == "__main__":
    tracemalloc.start()
    arr = ReadSampleData()
    k = 917
    position = BinarySearch(arr, k)
    # current, peak = tracemalloc.get_traced_memory()
    # print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    # tracemalloc.stop()
    if position == -1:
        print("Not found")
    else:
        print("Position: " + str(position))