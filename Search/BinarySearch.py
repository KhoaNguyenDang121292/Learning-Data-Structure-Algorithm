# Best case: O(1)
# Worst case: O(log(n))
# Average case: O(log(n))
# Time complexity: O(log(n))
# Space complexity: O(1)

import sys
sys.path.append("D:/DSaAlgo")

import tracemalloc
from read_sample import ReadSampleData

def BinarySearch(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low)//2
        if k < arr[mid]:
            high = mid - 1
        elif k > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    tracemalloc.start()
    arr = ReadSampleData()
    print(arr)
    k = 4
    print("K: " + str(k))
    position = BinarySearch(arr, k)
    # current, peak = tracemalloc.get_traced_memory()
    # print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    # tracemalloc.stop()
    if position == -1:
        print("Not found")
    else:
        print("Position: " + str(position))