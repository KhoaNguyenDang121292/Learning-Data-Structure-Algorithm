# def ReadSampleData():
#     with open("test_data.txt", "r") as f:
#         arr = f.readline().split()
#         arr = list(map(int, arr))
#     return arr
# Best case: Ascending array
# Worst case: Descending array
# Time complexity: O(n2)

# Best case: O(n)
# Worst case: O(n2)
# Average case: O(n2)
# Space complexity: O(1) - array includes 1 element only
import tracemalloc
from read_sample import ReadSampleData


def BubbleSortAsc(arr):
    i = len(arr) - 1
    while i >= 0:
        for j in range(0, i, +1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        i -= 1

def BubbleSortDesc(arr):
    i = len(arr) - 1
    while i >= 0:
        for j in range(0, i, +1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        i -= 1

def BubbleSortOptimize(arr):
    i = len(arr) - 1
    flag = 0 # Flag for swap or not
    while i >= 0:
        for j in range(0, i, +1):
            if arr[j] > arr[j+1]:
                flag = 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag == 0:
            break
        i -= 1

if __name__ == "__main__":
    tracemalloc.start()
    arr = ReadSampleData()
    BubbleSortAsc(arr)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    print(arr)