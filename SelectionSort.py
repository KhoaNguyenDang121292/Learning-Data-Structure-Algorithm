# Best case: array is sorted - O(n)
# Worst case: O(n2)
# Average case: O(n2)
# Time complexity: O(n2)
# Space complexity: O(1)

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

if __name__ == "__main__":
    arr = ReadSampleData()
    SelectionSortAsc(arr)
    print(arr)