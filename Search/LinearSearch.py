# Best case: O(1)
# Worst case: O(n)
# Average case: O(n/2)
# Time complexity: O(n2)
# Space complexity: O(1)
import tracemalloc
from read_sample import ReadSampleData

def LinearSearch(arr, k):
    i = 0
    while i < len(arr):
        if arr[i] == k:
            return i
        i += 1
    return -1

if __name__ == "__main__":
    tracemalloc.start()
    arr = ReadSampleData()
    k = 917
    position = LinearSearch(arr, k)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    if position == -1:
        print("Not found")
    else:
        print("Position: " + str(position))